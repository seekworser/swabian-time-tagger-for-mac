# -*- coding: utf-8 -*-
import views
import models


def show_top_window():
    w = views.TopWindow()
    w.new_action.triggered.connect(models.newTrigger)
    w.build_action.triggered.connect(lambda: show_build_output_browser(w))
    w.show()
    return w

def show_build_output_browser(parent):
    w = views.ShellStdoutBrowser(models.Builder())
    w.builder.moveToThread(w.build_thread)
    parent.dialogs.append(w)
    def show_in_browser(line):
        w.browser.append(line)
        return
    w.build_thread.started.connect(w.builder.build_docker_env)
    w.builder.build_output_yielded.connect(show_in_browser)
    w.show()
    w.build_thread.start()
    return