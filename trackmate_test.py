import sys

from ij import IJ
from ij import WindowManager

from fiji.plugin.trackmate import Model, Logger

# We have to do the following to avoid errors with UTF8 chars generated in 
# TrackMate that will mess with our Fiji Jython.
reload(sys)
sys.setdefaultencoding('utf-8')

# # Get currently selected image
# # imp = WindowManager.getCurrentImage()
imp = IJ.openImage('https://fiji.sc/samples/FakeTracks.tif')
# imp.show()

#----------------------------
# Create the model object now
#----------------------------
 
# Some of the parameters we configure below need to have
# a reference to the model at creation. So we create an
# empty model now.
 
model = Model()

# Send all messages to ImageJ log window.
model.setLogger(Logger.IJ_LOGGER)

print("complete Fiji Python script")