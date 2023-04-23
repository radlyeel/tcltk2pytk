#! /usr/bin/env python
# Tcl/Tk to OPython/Tkintet convereter
# Author: Daryl Lee
# Usage: $ ./tcltk2Pytk fname
#   where fname.tcl is a TCL/Tk file
#     and fname.py  is Python file using Tkinter to produce teh same lyout

import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: $ ./tcltk2Pytk fname");
        sys.exit( 1 )

    fname = sys.argv[1]
    print(f"processing {fname}.tcl")


