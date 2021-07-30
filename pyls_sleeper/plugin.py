import subprocess
from os import path, environ
from pyls import hookimpl
import logging

logger = logging.getLogger(__name__)

CALL_EXTERNAL = True # if True, use `subprocess` to shell out to a script and displaying the hang

@hookimpl
def pyls_lint(config, document):
    if not CALL_EXTERNAL:
        logger.warning(f"SLEEPER started")
        import time
        time.sleep(3.0)
        logger.warning(f"SLEEPER ending")
        return []

    sleeper_file = path.join(path.dirname(path.abspath(__file__)), 'ext', 'sleeper.py')

    proc = subprocess.Popen(["python", sleeper_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pid = proc.pid
    logger.warning(f"SLEEPER PID={pid} started")

    out_bytes, err_bytes = proc.communicate()

    logger.warning(f"SLEEPER PID={pid} DONE")

    return []
