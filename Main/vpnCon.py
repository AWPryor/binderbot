import subprocess
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
k = os.path.dirname(dir_path)
subprocess.call([k])
