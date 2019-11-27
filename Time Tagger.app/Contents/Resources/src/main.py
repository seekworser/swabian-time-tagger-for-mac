# -*- coding: utf-8 -*-
import sys
import docker
import PySide2.QtWidgets as qw
import controllers


def main():
    app = qw.QApplication(sys.argv)
    _ = controllers.show_top_window()
    sys.exit(app.exec_())
    return

if __name__ == "__main__":
    main()