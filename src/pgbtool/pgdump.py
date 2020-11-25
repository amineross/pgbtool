import subprocess
import sys

# Interacting with external process pg_dump
def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f'Error: {err}')
        sys.exit(1)
