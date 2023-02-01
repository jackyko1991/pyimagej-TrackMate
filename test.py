#@ ImagePlus imp
#@ output int foo
#@ output float bar
#@ output shape
import sys

from ij import IJ
from ij import WindowManager

"""
parameter input and output parsing can refer to the syntax documentation: https://imagej.net/scripting/parameters.
#@output Type outputName will declare the variable of the specified name as an output parameter with the given type. 
The Type parameter is optional, as the output will be treated as Object be default. 
"""

# We have to do the following to avoid errors with UTF8 chars generated in 
# TrackMate that will mess with our Fiji Jython.
reload(sys)
sys.setdefaultencoding('utf-8')

imp.show() # you have to use interative mode in pyimagej to trigger this line
hello = 1
bar = 0.1
shape = imp.getDimensions()

print("complete Fiji Python script")