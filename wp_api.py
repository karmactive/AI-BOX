#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared WordPress REST helper for the karmactive pipeline.

Single source of truth for auth, retries, and the context=edit query join.
Credential comes from KARMACTIVE_WP_AUTH ("user:app password") when set,
so scripts need not carry it inline.
"""
import base64, json, os, subprocess, time

SITE = "https://www.karmactive.com"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
_FALLBACK = None  # Credentials come from KARMACTIVE_WP_AUTH env var only
_wp_auth_env = os.environ.get("KARMACTIVE_WP_AUTH")
if not _wp_auth_env:
    print("ERROR: KARMACTIVE_WP_AUTH environment variable not set.")
    print("Usage: export KARMACTIVE_WP_AUTH=\"user:app-password\"")
    import sys; sys.exit(1)
AUTH = base64.b64encode(_wp_auth_env.encode()).decode()


def _url(path, ctx):
    url = "%s/wp-json/wp/v2/%s" % (SITE, path)
    return url + (("&" if "?" in path else "?") + "context=edit" if ctx else "")


def api(method, path, data=None, ctx=False, retries=5):
    """Call the REST API and return parsed JSON. Raises SystemExit on exhaustion."""
    args = ["curl", "-s", "--retry", "5", "--retry-delay", "2",
            "--connect-timeout", "30", "--max-time", "180",
            "-A", UA, "-H", "Authorization: Basic " + AUTH, "-X", method]
    if data is not None:
        args += ["-H", "Content-Type: application/json",
                 "--data", json.dumps(data, ensure_ascii=False)]
    args.append(_url(path, ctx))
    for attempt in range(retries):
        out = subprocess.run(args, capture_output=True, text=True, timeout=240)
        if out.returncode == 0 and out.stdout.strip():
            try:
                return json.loads(out.stdout)
            except ValueError:
                pass
        time.sleep(2)
    raise SystemExit("API FAIL %s %s" % (method, path))


def upload_media(path, mime):
    """Upload a local file to the media library; returns the media object."""
    args = ["curl", "-s", "--retry", "5", "--retry-delay", "2",
            "--connect-timeout", "30", "--max-time", "240",
            "-A", UA, "-H", "Authorization: Basic " + AUTH,
            "-H", "Content-Disposition: attachment; filename=%s" % os.path.basename(path),
            "-H", "Content-Type: %s" % mime,
            "--data-binary", "@" + path, SITE + "/wp-json/wp/v2/media"]
    for attempt in range(5):
        out = subprocess.run(args, capture_output=True, text=True, timeout=300)
        if out.returncode == 0 and out.stdout.strip():
            try:
                return json.loads(out.stdout)
            except ValueError:
                pass
        time.sleep(3)
    raise SystemExit("UPLOAD FAIL %s" % path)
