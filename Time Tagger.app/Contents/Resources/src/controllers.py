# -*- coding: utf-8 -*-
import views
import models
from parameters import *


def startup(parent):
    starter = models.CommandLineRunner("\"" + START_FILE + "\"")
    start_thread = qc.QThread(parent=parent)
    w = views.ShellStdoutLabel(parent)
    starter.moveToThread(start_thread)
    w.object_collection.update({w.__hash__: w, hash(starter): starter, hash(start_thread): start_thread})
    w.parent.object_collection.update(w.object_collection)
    start_thread.started.connect(starter.run)
    starter.output_yielded.connect(w.label.setText)
    starter.process_end.connect(start_thread.terminate)
    starter.process_end.connect(w.close)
    w.show()
    start_thread.start()
    return

def show_top_window():
    w = views.TopWindow()
    startup(w)
    w.new_action.triggered.connect(models.newTrigger)
    w.build_action.triggered.connect(lambda: show_build_output_browser(w))
    w.on_close.connect(models.stop_machine)
    w.show()
    return w

def show_build_output_browser(parent):
    builder = models.CommandLineRunner("\"" + BUILD_FILE + "\"")
    build_thread = qc.QThread(parent=parent)
    w = views.ShellStdoutBrowser(parent)
    builder.moveToThread(build_thread)
    w.object_collection.update({w.__hash__: w, hash(builder): builder, hash(build_thread): build_thread})
    w.parent.object_collection.update(w.object_collection)
    build_thread.started.connect(builder.run)
    builder.output_yielded.connect(w.browser.append)
    builder.process_end.connect(build_thread.terminate)
    w.show()
    build_thread.start()
    return