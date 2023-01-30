import sys
import os
import imagej
import imagej.doctor

def main():
    # export JAVA_HOME path for the virtual environment
    # if JAVA_HOME is not set and we are in a conda environment
    if (not os.environ.get('JAVA_HOME')) and os.environ.get('CONDA_DEFAULT_ENV'):
        # infer the conda environment via sys.executable path
        os.environ['JAVA_HOME'] = os.sep.join(sys.executable.split(os.sep)[:-1] + ['Library'])
    
    imagej.doctor.checkup()

    FIJI_DIR = "C:/Users/kko/Software/Fiji.app"

    print("Initializing Fiji on JVM...")
    ij = imagej.init(FIJI_DIR,mode='headless')
    print(ij.getApp().getInfo(True))

if __name__=="__main__":
    main()