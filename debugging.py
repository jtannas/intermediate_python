"""Python Debugger Introduction

$ python -m pdb my_script.py
    or
Set the debugging stops in the script

Docs: https://docs.python.org/3/library/pdb.html

Commands:
c: continue execution
w: shows the context of the current line it is executing.
a: print the argument list of the current function
s: Execute the current line and stop at the first possible occasion.
n: Continue execution until the next line in the current function is reached or it returns.
"""

import pdb


def make_bread():
    """PDB set_trace example"""
    pdb.set_trace()
    return "I don't have time"


s

print(make_bread())
