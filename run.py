#!/usr/bin/env python

"""run.py: entrypoint"""

__author__      = "oleting, Weckyy702"

from gui.gui import Gui as gui
from sys import argv

do_debug = "--debug" in argv

gui(theme='DarkGrey11', debug_mode=do_debug)