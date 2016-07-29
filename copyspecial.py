#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def getSpecialPaths(destdir):    
    filenames = os.listdir(destdir)
    regex = re.compile("__\w+__")
    x = [os.path.abspath(os.path.join(destdir, filename)) for filename in filenames for m in [regex.search(filename)] if m]
    return x


def copyTo(path, destdir):
    paths = getSpecialPaths(path)    
    for p in paths:
        if os.path.isdir(destdir):
            shutil.copy(p, destdir)
        else: 
            os.makedirs(destdir) # create all directories, raise an error if it already exists
            shutil.copy(p, destdir)

            
def zipTo(paths, zippath):
   
   

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
