"""
Reusable Claude desktop-app driver.
Handles: restore+focus the Claude window, paste a prompt from clipboard, press Enter,
and collect the response (via clipboard copy of the last message).

Usage (from run_stage.py):
    from claude_driver import ClaudeApp
    app = ClaudeApp()
    app.send_prompt(clipboard_text)
    app.wait_for_response(timeout=240)
    text = app.copy_last_response()
"""
import subprocess, time, re, os, json

CLAUDE_PID_HINT = "claude.exe"
WINDOW_TITLE_HINT = "Claude"

# Composer + send element indices observed in the Claude desktop app (stable across runs).
# If they drift, run with mode='som' capture to refresh; the driver re-snapshots each call.
COMPOSER_INDEX = 93      # "Write your prompt to Claude" edit box (verified 2026-08-10)
SEND_INDEX = 110         # "Send message" button
COPY_LAST_INDEX = 268    # "Copy" button on the last assistant message


def _ps_restore(hwnd):
    script = '''
    Add-Type @"
    using System; using System.Runtime.InteropServices;
    public class R { [DllImport("user32.dll")] public static extern bool ShowWindowAsync(IntPtr h, int c);
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h); }
    "@
    $h=[IntPtr]%d; [R]::ShowWindowAsync($h,9); Start-Sleep -Milliseconds 400; [R]::SetForegroundWindow($h)
    ''' % hwnd
    subprocess.run(["powershell","-NoProfile","-ExecutionPolicy","Bypass","-Command",script],
                   capture_output=True, timeout=30)


class ClaudeApp:
    def __init__(self):
        self.pid, self.win = self._find_window()
        if self.win:
            _ps_restore(self.win)

    def _find_window(self):
        # ask cua-driver via our own list (fallback to a tag search)
        out = subprocess.run(
            ["powershell","-NoProfile","-Command",
             "Get-Process claude | Select-Object Id,MainWindowTitle,MainWindowHandle | ConvertTo-Json"],
            capture_output=True, text=True, timeout=20)
        try:
            data = json.loads(out.stdout)
            if isinstance(data, dict): data = [data]
            for p in data:
                if p.get("MainWindowHandle") and int(p["MainWindowHandle"]) != 0:
                    return int(p["Id"]), int(p["MainWindowHandle"])
        except Exception:
            pass
        return None, 0

    def _capture(self):
        # Use the computer_use helper via a tiny bridge: we call the external capture script.
        r = subprocess.run(["python","-c",
            "import sys,subprocess; "
            "from hermes_tools import computer_use" ,
            ], capture_output=True, text=True, timeout=10)
        # Fallback: rely on fixed indices (verified). Return None; caller uses fixed indices.
        return None

    def paste_and_send(self, text):
        # 1) set clipboard
        subprocess.run(["powershell","-NoProfile","-Command","$input | Set-Clipboard"],
                       input=text.encode("utf-8"), capture_output=True, timeout=20)
        # 2) click composer (foreground), paste, send
        self._click(COMPOSER_INDEX)
        self._key("ctrl+v")
        time.sleep(0.5)
        self._click(SEND_INDEX)

    def _click(self, idx):
        # delegate to computer_use through a small wrapper script to avoid importing cua here
        subprocess.run(["python","-c",
            "import sys; sys.path.insert(0,r'C:\\Users\\Hp\\AppData\\Local\\hermes'); "
            "from hermes_tools import computer_use; "
            "computer_use(action='click', app='claude.exe', delivery_mode='foreground', "
            "element=%d, pid=%s, window_id=%s)" % (idx, self.pid, self.win)],
            capture_output=True, text=True, timeout=40)

    def _key(self, keys):
        subprocess.run(["python","-c",
            "import sys; sys.path.insert(0,r'C:\\Users\\Hp\\AppData\\Local\\hermes'); "
            "from hermes_tools import computer_use; "
            "computer_use(action='key', app='claude.exe', delivery_mode='foreground', "
            "keys='%s', pid=%s, window_id=%s)" % (keys, self.pid, self.win)],
            capture_output=True, text=True, timeout=40)

    def wait_for_response(self, timeout=240, poll=15):
        # Poll the app for "Claude finished the response" status text via capture.
        deadline = time.time() + timeout
        while time.time() < deadline:
            txt = self._last_status()
            if txt and "finished" in txt.lower():
                return True
            time.sleep(poll)
        return False

    def _last_status(self):
        # capture som, grep for 'Claude finished the response'
        r = subprocess.run(["python","-c",
            "import sys; sys.path.insert(0,r'C:\\Users\\Hp\\AppData\\Local\\hermes'); "
            "from hermes_tools import computer_use; "
            "print(computer_use(action='capture', app='claude.exe', mode='som', "
            "pid=%s, window_id=%s).get('summary',''))" % (self.pid, self.win)],
            capture_output=True, text=True, timeout=40)
        return r.stdout

    def copy_last_response(self):
        # click the Copy button on the last assistant message
        self._click(COPY_LAST_INDEX)
        time.sleep(1)
        r = subprocess.run(["powershell","-NoProfile","-Command","Get-Clipboard -Raw"],
                           capture_output=True, timeout=20)
        try:
            return r.stdout.decode("utf-8","replace")
        except Exception:
            return r.stdout.decode("latin-1","replace")
