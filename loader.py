from glob import glob

files = glob("*.py")

text = ""
for file in files:
    if not file.endswith("loader.py"):
        with open(file,'r') as f:
            text += "###################\n#" + file.upper() + "\n###################\n\n" + f.read()

with open("/home/mathigatti/.local/lib/python3.8/site-packages/FoxDot/lib/Custom/startup.py",'w') as f:
    f.write(text)