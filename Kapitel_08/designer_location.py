import sys
import os

path = os.path.split(sys.executable)
libs = path[0] + "/Library/bin"
os.environ["PATH"] = os.environ["PATH"] + ";" + libs

from PyQt5.QtWebEngineWidgets import *


