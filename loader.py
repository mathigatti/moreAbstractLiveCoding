from glob import glob

files = glob("*.py")

text = ""
for file in files:
    if not file.endswith("loader.py"):
        with open(file,'r') as f:
            text += "###################\n#" + file.upper() + "\n###################\n\n" + f.read()


from FoxDot import FOXDOT_ROOT
import os

with open(os.path.join(FOXDOT_ROOT,"lib/Custom/startup.py"),'w') as f:
    f.write(text)
