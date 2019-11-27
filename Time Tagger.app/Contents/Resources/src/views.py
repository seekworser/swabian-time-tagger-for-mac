# -*- coding: utf-8 -*-
import PySide2.QtWidgets as qw
import PySide2.QtCore as qc
import PySide2.QtGui as qg
from parameters import *
import typing


class TopWindow(qw.QMainWindow):
    on_close = qc.Signal()
    def __init__(self, parent=None):

        super().__init__(parent)
        self.object_collection: typing.Dict[int, object] = dict()

        self.title_label = qw.QLabel('<p><font size="4">Swabian Time Tagger for Mac</font></p>')
        self.title_label.setAlignment(qc.Qt.AlignCenter)
        self.open_python_shell = qw.QPushButton("Open Python interactive shell")
        self.run_python_file = qw.QPushButton("Run Python file")
        self.open_web_application = qw.QPushButton("Open web application")
        self.ssh_vm = qw.QPushButton("SSH connect to VM")

        window = qw.QWidget()
        layout = qw.QBoxLayout(qw.QBoxLayout.TopToBottom)
        layout.addWidget(self.title_label)
        layout.addWidget(self.open_python_shell)
        layout.addWidget(self.run_python_file)
        layout.addWidget(self.open_web_application)
        layout.addWidget(self.ssh_vm)
        window.setLayout(layout)
        self.setCentralWidget(window)

        mbar = self.menuBar()
        self.file_menu = mbar.addMenu("File")
        self.new_action = qw.QAction("New", self)
        self.file_menu.addAction(self.new_action)
        self.new_action.setShortcut("Ctrl+N")
        self.build_action = qw.QAction("Build", self)
        self.file_menu.addAction(self.build_action)
        self.build_action.setShortcut("Ctrl+B")

        self.move(100, 100)

    def closeEvent(self, event):
        self.on_close.emit()
        super().closeEvent(event)
        return

class TopWindowChildDialog(qw.QDialog):
    def __init__(self, parent: TopWindow):
        super().__init__(parent)
        self.parent = parent
        self.parent.hide()
        self.object_collection: typing.Dict[int, object] = dict()

    def reject(self):
        for item in self.object_collection.keys():
            self.parent.object_collection.pop(item)
        self.parent.show()
        super().reject()
        return


class ShellStdoutLabel(TopWindowChildDialog):
    def __init__(self, parent: TopWindow):
        super().__init__(parent)
        self.label = qw.QLabel()
        layout = qw.QBoxLayout(qw.QBoxLayout.TopToBottom)
        layout.addWidget(self.label)
        self.setLayout(layout)
        return

class ShellStdoutBrowser(qw.QDialog):
    def __init__(self, parent: TopWindow):
        super().__init__(parent)
        self.browser = qw.QTextBrowser()
        layout = qw.QBoxLayout(qw.QBoxLayout.TopToBottom)
        layout.addWidget(self.browser)
        self.setLayout(layout)
        return

class PythonShellWindow(qw.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
