import os
import subprocess
import appscript
import docker
import PySide2.QtWidgets as qw
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
            self.output_yielded.emit(line.decode().strip())
        self.process_end.emit()
        return

def stop_machine():
    for line in run_with_line_get(cmd="\"" + CLOSE_FILE + "\""):
        print(line.decode(), end="")

def open_python_shell():
    command = (
        "docker $(docker-machine config swabian-time-tagger) run --rm --privileged -ti swabian-time-tagger ipython"
    )
    appscript.app("Terminal").do_script(command)
    return

def run_python_file(parent):
    options = qw.QFileDialog.Options()
    # options |= qw.QFileDialog.DontUseNativeDialog
    path_name, _ = qw.QFileDialog.getOpenFileName(
        parent,
        "qw.QFileDialog.getOpenFileName()",
        os.environ["HOME"],
        "Python Files (*.py);;All Files (*)",
        options=options
    )
    dir_name, file_name = os.path.split(path_name)
    if not file_name:
        return dir_name, file_name
    config = subprocess.Popen(
        ["docker-machine", "config", "swabian-time-tagger"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8"
    )
    config_string = [item.strip() for item in config.stdout.readlines()]
    command = [
        "docker",
        *config_string,
        "run",
        "-it",
        "-v=" + dir_name.strip() + ":/wd",
        "--rm",
        "--privileged",
        "swabian-time-tagger",
        "bash",
        "-c",
        "cd /wd; python3 " + file_name.strip()
    ]
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8") as proc:
        print("open")
        w = qw.QMessageBox(text="stdout: " + proc.stdout.read())
        print(w)
        w.exec_()
        w = qw.QMessageBox(text="stderr: " + proc.stderr.read())
        print(w)
        w.exec_()
    return