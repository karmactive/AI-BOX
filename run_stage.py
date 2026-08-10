"""
run_stage.py <story> <stage>  -- one command to run a pipeline stage in the Claude app.

Pre-conditions (staged beforehand):
  - trial-<story>/stage<stage>_prompt.md exists (the instruction block for this stage)
  - Claude desktop app is logged in and on screen
This script: loads the prompt, pastes to Claude, sends, waits for completion,
copies the response, saves to trial-<story>/stage<stage>_output.md, and commits+pushes.

Stage prompts to pre-write (per story):
  stage2_prompt.md  -> draft
  stage3b_prompt.md -> apply fact-check corrections
  stage4_prompt.md  -> SEO package (title, meta, categories, tags, slug)
  stage5_prompt.md  -> final packaging + internal/external links
"""
import sys, subprocess, pathlib, time

REPO = pathlib.Path(r"C:\Users\Hp\OneDrive\karmactive-pipeline")
sys.path.insert(0, str(REPO))
from claude_driver import ClaudeApp

STORY = sys.argv[1] if len(sys.argv) > 1 else "colombia-quake-aug10"
STAGE = sys.argv[2] if len(sys.argv) > 2 else "2"
FOLDER = REPO / f"trial-{STORY}"
PROMPT = FOLDER / f"stage{STAGE}_prompt.md"
OUT = FOLDER / f"stage{STAGE}_output.md"

assert PROMPT.exists(), f"missing {PROMPT}"

text = PROMPT.read_text(encoding="utf-8")
print(f"[run_stage] {STORY} stage {STAGE}: prompt {len(text)} chars")

app = ClaudeApp()
app.paste_and_send(text)
print("[run_stage] sent. waiting for Claude to finish...")
done = app.wait_for_response(timeout=300, poll=20)
print("[run_stage] finished:", done)

resp = app.copy_last_response()
OUT.write_text(resp, encoding="utf-8")
print(f"[run_stage] saved {OUT} ({len(resp)} chars)")

# commit + push
subprocess.run(["git","-C",str(REPO),"add","-A"], timeout=30)
subprocess.run(["git","-C",str(REPO),"-c","user.name=Hermes Agent","-c","user.email=hermes@local",
                "commit","-q","-m",f"{STORY}: Stage {STAGE} output (Claude app)"], timeout=30)
p = subprocess.run(["git","-C",str(REPO),"push","origin","hermes-pipeline"],
                   capture_output=True, text=True, timeout=90)
print("[run_stage] push rc:", p.returncode, p.stdout.strip()[-120:], p.stderr.strip()[-120:])
