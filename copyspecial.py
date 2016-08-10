#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
from zipfile import *


"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def getSpecialPaths(destdir):    
    filenames = os.listdir(destdir)
    regex = re.compile("__\w+__")
    paths = [os.path.abspath(os.path.join(destdir, filename)) for filename in filenames for m in [regex.search(filename)] if m]
    return paths


def copyTo(path, destdir):
    if not os.path.exists(destdir):
        os.makedirs(destdir)
    for p in path:
            shutil.copy(p, destdir)

            
def zipTo(path, zippath):
   zf = ZipFile("%s.zip" % (zippath), "w", zipfile.ZIP_DEFLATED)
   absPath = os.path.abspath(path)
   for dirname, subdirs, files in os.walk(path):
       for filename in files:
           absname = os.path.abspath(os.path.join(dirname, filename))
           arcname = absname[len(absPath) + 1:]
           print 'zipping %s as %s' % (os.path.join(dirname, filename), arcname)
           zf.write(absname, arcname)
   zf.close
            
