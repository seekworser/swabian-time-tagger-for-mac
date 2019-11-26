# -*- coding: utf-8 -*-
import views
import models


def show_top_window():
    w = views.TopWindow()
    w.new_action.triggered.connect(models.newTrigger)
    w.show()
    return w