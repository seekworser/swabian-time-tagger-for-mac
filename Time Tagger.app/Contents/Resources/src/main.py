# -*- coding: utf-8 -*-
import sys
import PySide2.QtWidgets as qw
import controllers
import views


def main():
    app = qw.QApplication(sys.argv)
    _ = controllers.show_top_window()
    sys.exit(app.exec_())
    return

if __name__ == "__main__":
    main()