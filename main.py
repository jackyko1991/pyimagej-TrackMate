import sys
import os
import imagej
import imagej.doctor
import scyjava as sj

# macro = """
# import sys

# from ij import IJ
# from ij import WindowManager

# from fiji.plugin.trackmate import Model, Logger

# # We have to do the following to avoid errors with UTF8 chars generated in 
# # TrackMate that will mess with our Fiji Jython.
# reload(sys)
# sys.setdefaultencoding('utf-8')

# # # Get currently selected image
# # # imp = WindowManager.getCurrentImage()
# imp = IJ.openImage('https://fiji.sc/samples/FakeTracks.tif')
# imp.show()

# #----------------------------
# # Create the model object now
# #----------------------------

# # Some of the parameters we configure below need to have
# # a reference to the model at creation. So we create an
# # empty model now.

# model = Model()

# # Send all messages to ImageJ log window.
# model.setLogger(Logger.IJ_LOGGER)
# """


def main():
    # export JAVA_HOME path for the virtual environment
    # if JAVA_HOME is not set and we are in a conda environment
    if (not os.environ.get('JAVA_HOME')) and os.environ.get('CONDA_DEFAULT_ENV'):
        # infer the conda environment via sys.executable path
        os.environ['JAVA_HOME'] = os.sep.join(sys.executable.split(os.sep)[:-1] + ['Library'])
    
    imagej.doctor.checkup()

    FIJI_DIR = "C:/Users/kko/Software/Fiji.app"
    IMAGE_PATH = "I:/Group Fritzsche/Jacky/tcell/1To2CancerToTcell_ratio/C1_Nyeso1HCT116_1G4PrimaryPure_Icam_CxCl12_CellTrackerDeepRed_640nm_Tcells_T1-30.tif"

    # ImageJ Macro has to be load before initialization
    with open("test.ijm","r") as f:
        macro_ijm = f.read()

    with open("trackmate_test.py","r") as f:
        macro_py = f.read()

    print("Initializing Fiji on JVM...")
    ij = imagej.init(FIJI_DIR,mode='headless')
    # ij = imagej.init(FIJI_DIR,mode='interactive')
    print(ij.getApp().getInfo(True))

    print("ImageJ loading ...")
    # im = ij.io().open(IMAGE_PATH)
    # im = ij.io().open('https://samples.fiji.sc/FakeTracks.tif')
    # imp = ij.py.to_imageplus(im)
    # ij.py.window_manager().setTempCurrentImage(imp)
    # print("Starting TrackMate GUI...")
    # ij.py.run_plugin('TrackMate', {})

    # import TrackMate via scyjava
    # TrackMate = sj.jimport('fiji.plugin.trackmate.TrackMate')

    # loading fiji script from file
    args = {
        'name': 'Chuckles',
        'age': 13,
        'city': 'nowhere'
    }

    task = ij.py.run_script('ijm', macro_ijm, args)
    task = ij.py.run_script('python', macro_py, args)

    print(task.getOutput('greeting'))
    
if __name__=="__main__":
    main()