import subprocess
import appscript
import docker
import PySide2.QtCore as qc
from parameters import *


def run_with_line_get(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        line = proc.stdout.readline()
        if line:
            yield line
        if not line and proc.poll() is not None:
            break
    return

class CommandLineRunner(qc.QObject):
    output_yielded = qc.Signal(str)
    process_end = qc.Signal()
    def __init__(self, fname):
        super().__init__()
        self.fname = fname
        return

    def run(self):
        for line in run_with_line_get(self.fname):
            print(line.decode(), end="")
            self.output_yielded.emit(line.decode())
        self.process_end.emit()
        return

def stop_machine():
    for line in run_with_line_get(cmd="\"" + CLOSE_FILE + "\""):
        print(line.decode(), end="")

def open_python_shell():
    command = (
        "docker $(docker-machine config swabian-time-tagger) run --rm -ti swabian-time-tagger bash\n"
        "ipython"
    )
    appscript.app("Terminal").do_script(command)
    return

def newTrigger():
    print("New is triggered")
    return
