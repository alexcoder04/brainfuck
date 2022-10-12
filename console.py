#!/usr/bin/env python3

import os
import sys
from interpreter import Interpreter

AUTORUN_FILE = os.path.join(os.getenv("XDG_CONFIG_HOME"), "bf", "bfrc") # file to run every time the interpreter starts

# IFMAIN
if __name__ == "__main__":
    # create a new interpreter
    interpreter = Interpreter()
    # run the autorun script
    if os.path.isfile(AUTORUN_FILE):
        interpreter.run_file(AUTORUN_FILE)
    # check if a file is provided in arguments
    for arg in sys.argv:
        # if so run it
        if arg.endswith(".bf"):
            interpreter.run_file(arg)
            break
    else:
        # start the console
        interpreter.console()
