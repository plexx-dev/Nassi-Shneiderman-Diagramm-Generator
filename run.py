#!/usr/bin/env python
# from gui.gui import Gui
# import sys

# do_debug = "--debug" in sys.argv

# Gui(theme='DarkGrey11', debug_mode=do_debug)

# Web App
from Web import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=5000 ,debug=True)