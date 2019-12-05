import os
import PySide2.QtCore as qc


DOCKER_MACHINE_NAME = "swabian-time-tagger"
DOCKER_IMAGE_NAME = "swabian-time-tagger"
RESOURCES_DIR = os.path.dirname(os.path.dirname(__file__))
DOCKER_FILE_DIR = RESOURCES_DIR + "/swabian-time-tagger-dockerfile"
BUILD_FILE = DOCKER_FILE_DIR + "/build"
START_FILE = DOCKER_FILE_DIR + "/start"
CLOSE_FILE = DOCKER_FILE_DIR + "/close"
