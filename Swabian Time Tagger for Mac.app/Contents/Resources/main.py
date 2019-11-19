# -*- coding: utf-8 -*-
import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtGui as qg


class MainWindow(qw.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        mbar = self.menuBar()
        file = mbar.addMenu("File")
        newAction = qw.QAction("New", self)
        newAction.setShortcut("Ctrl+N")
        file.addAction(newAction)
        newAction.triggered.connect(self.newTrigger)

    def newTrigger(self):
        print("New is triggered")

def main():
    app = qw.QApplication([sys.argv])
    w = MainWindow()
    w.show()
    app.exec_()
    return

if __name__ == "__main__":
    main()