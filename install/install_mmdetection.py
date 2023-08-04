import os
import subprocess

# Move back to the previous directory
os.chdir("..")

# Clone mmdetection repository
if os.path.exists("mmdetection"):
    os.system("rm -rf mmdetection")

subprocess.run(["git", "clone", "https://github.com/open-mmlab/mmdetection.git"])

# Move into mmdetection directory
os.chdir("mmdetection")

# Install mmdetection in editable mode
subprocess.run(["pip", "install", "-e", "."])

# Move back to the previous directory
os.chdir("..")
