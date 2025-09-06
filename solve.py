import subprocess, sys

try:
    out = subprocess.check_output(['/readflag'])
    # Print to stdout so the web UI shows the flag inside <pre>…</pre>
    sys.stdout.write(out.decode('utf-8', errors='ignore'))
except Exception as e:
    print("ERR:", e)