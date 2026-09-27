import contextlib
import io
import runpy
import sys


def run(path, stdin=""):
    out = io.StringIO()
    old = sys.stdin
    sys.stdin = io.StringIO(stdin)
    try:
        with contextlib.redirect_stdout(out):
            env = runpy.run_path(path)
    finally:
        sys.stdin = old
    return env, out.getvalue()
