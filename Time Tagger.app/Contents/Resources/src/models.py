import subprocess
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

class Builder(qc.QObject):
    build_output_yielded = qc.Signal(str)
    process_end = qc.Signal()
    def build_docker_env(self):
        for line in run_with_line_get(cmd="\"" + BUILD_FILE + "\""):
            self.build_output_yielded.emit(line.decode())
        self.process_end.emit()
        return

def start_container():
    return

def newTrigger():
    print("New is triggered")
    return
