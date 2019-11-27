# -*- coding: utf-8 -*-
import PySide2.QtWidgets as qw
import PySide2.QtCore as qc
import PySide2.QtGui as qg


class TopWindow(qw.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.childs = dict()

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

class ShellStdoutBrowser(qw.QDialog):
    def __init__(self, builder: qc.QObject, parent: TopWindow):
        super().__init__(parent)

        self.browser = qw.QTextBrowser()

        layout = qw.QBoxLayout(qw.QBoxLayout.TopToBottom)
        layout.addWidget(self.browser)
        self.setLayout(layout)

        self.builder = builder
        self.build_thread = qc.QThread()
        return

    def closeEvent(self, event: qg.QCloseEvent):
        self.parent.childs.pop(self.__hash__)
        super().closeEvent(event)
        return

class PythonShellWindow(qw.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
