# CCS model transition from .lib to .db by Library Compiler

There are 180 files in LIB/CCS folder.

Library Compiler can transform 124 files in default, and there are a few problems in the rest of .lib files (all *SEQ*.lib (36 files) and a part of *ccsa*.lib (20 files)).

Solutions:

 - Integrated clock-gater (ICG) cells in *SEQ*.lib are commented out.

 - Libary name *ccsp* in 20 *cca*.lib are changed to *ccsa*.

Additions:
 - compare.py is to find 56 files.
 - SEQ.py is to comment out Integrated clock-gater (ICG) cells.
 - lc.tcl is a script for Library Compiler.
