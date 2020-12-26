from gui.gui import Gui
import sys

do_debug = False

if len(sys.argv) > 1:
    if sys.argv[1] == "--debug":
        do_debug = True

Gui(theme='DarkGrey11', debug_mode=do_debug)