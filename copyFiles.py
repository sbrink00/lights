import os
import shutil

def hasBadEnding(string):
  if string == "copyFiles.py": return True
  for ending in badEndings:
    if ending in string: return True
  return False

oldDir = input("What directory do you want to copy files from? ") + "/"
if os.path.exists("/Users/god/Desktop/graphics/" + oldDir + "__pycache__"):
  shutil.rmtree("/Users/god/Desktop/graphics/" + oldDir + "__pycache__")
files = os.listdir("/Users/god/Desktop/graphics/" + oldDir)
badEndings = [".md", ".pyc", ".png", ".ppm", ".git"]

files = [x for x in files if not hasBadEnding(x)]
for i in files:
  f = open("/Users/god/Desktop/graphics/" + oldDir + i, "r")
  f1 = open(i, "w")
  s = f.read()
  f1.write(s)
  f.close()
  f1.close()
