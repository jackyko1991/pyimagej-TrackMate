import sys
import os
import imagej
import imagej.doctor
import scyjava as sj
from skimage import io

def main():
    headless = True

    # The local working path need to be stored as pyimagej will change the CWD after initialization
    CWD = os.getcwd()

    # export JAVA_HOME path for the virtual environment
    # if JAVA_HOME is not set and we are in a conda environment
    if (not os.environ.get('JAVA_HOME')) and os.environ.get('CONDA_DEFAULT_ENV'):
        # infer the conda environment via sys.executable path
        os.environ['JAVA_HOME'] = os.sep.join(sys.executable.split(os.sep)[:-1] + ['Library'])
    
    imagej.doctor.checkup()

    FIJI_DIR = "C:/Users/kko/Software/Fiji.app"
    # IMAGE_PATH = "I:/Group Fritzsche/Jacky/tcell/1To2CancerToTcell_ratio/C1_Nyeso1HCT116_1G4PrimaryPure_Icam_CxCl12_CellTrackerDeepRed_640nm_Tcells_T1-30.tif"
    IMAGE_PATH = "https://fiji.sc/samples/FakeTracks.tif"

    print("Initializing Fiji on JVM...")
    if headless:
        ij = imagej.init(FIJI_DIR,mode='headless')
    else:
        ij = imagej.init(FIJI_DIR,mode='interactive')
    print(ij.getApp().getInfo(True))

    print("Image loading on python side...")
    image = io.imread(IMAGE_PATH)
    imp = ij.py.to_imageplus(image)

    if not headless:
        ij.ui().showUI()
        ij.ui().show(imp)
        input("Press Enter to continue...")

    File = sj.jimport('java.io.File')
    jfile = File(os.path.join(CWD,'trackmate.py'))

    # convert python side stuffs to java side
    # define python side arguments
    args = {
        'imp': imp, # java side ImagePlus object
        'headless': headless
    }
    jargs = ij.py.jargs(args)
    result_future = ij.script().run(jfile,True,jargs)

    # get the result from java future, blocking will occur here
    result = result_future.get()
    if not headless:
        input("Press Enter to continue...")
    print(ij.py.from_java(result.getOutput("foo")))
    print(ij.py.from_java(result.getOutput("bar")))
    print(ij.py.from_java(result.getOutput("shape")))
    
    
if __name__=="__main__":
    main()