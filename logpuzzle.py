#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import pandas as pd
"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  os.chdir('C:\Users\Matt Green\Desktop\googlePythonExercises')
  uf = urllib.urlopen(filename) # opening the url/webpage
  ufSource = uf.readlines()     # reading each line as seperate item in a list
  uf.close()    # closing the file/url
  regex = re.compile("(GET\s)(.+google-python-class/images/puzzle.+)(\sHTTP)")  # creating a regular expression to filter out what we want from each line
  urls = [m.group(2) for line in ufSource for m in [regex.search(line)] if m]   #creating list of partial urls
  urls = set(urls)  # removing all duplicates
  urls = list(urls) # changing set back into a list
  urls.sort()       # sorting the urls in alphabetical order
  fullurls = []     # empty list to be filled with the full, alphabetized urls    
  for url in urls:  # creating the lsit of fullurls
      newurl = 'http://code.google.com' + url  # combining the base url with the partial urls found in the filename 
      fullurls.append(newurl)   # appending the fullurls list with the full urls of each item in urls          
  return fullurls  # returning the lsit of full urls to the end user
  

def read_urls2(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  os.chdir('C:\Users\Matt Green\Desktop\googlePythonExercises')
  uf = urllib.urlopen(filename) # opening the url/webpage
  ufSource = uf.readlines()     # reading each line as seperate item in a list
  uf.close()    # closing the file/url
  regex = re.compile("(GET\s)(.+google-python-class/images/puzzle.+)(\w-.+)(-.+)(\sHTTP)")  # creating a regular expression to filter out what we want from each line
  surls = [m.group(3) for line in ufSource for m in [regex.search(line)] if m]   #creating list of partial urls
  eurls = [m.group(4) for line in ufSource for m in [regex.search(line)] if m]   #creating list of partial urls
  urls = pd.DataFrame(eurls, surls)  
  urls = urls.drop_duplicates()  # removing all duplicates
  urls = urls.sort(0)       # sorting the urls in alphabetical order
  fullurls = []     # empty list to be filled with the full, alphabetized urls    
  for i in range(len(urls)):  # creating the lsit of fullurls   
      newurl = 'http://developers.google.com/edu/python/images/puzzle/' + urls.index.values[i] + urls[0][i]  # combining the base url with the partial urls found in the filename
      fullurls.append(newurl)   # appending the fullurls list with the full urls of each item in urls               
  return fullurls  # returning the lsit of full urls to the end user
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.isdir(dest_dir):
      os.makedirs(dest_dir) # create all directories, raise an error if it already exists  
  
  index = file(os.path.join(dest_dir, 'index.html'), 'w')   # creating a new html file for the index
  index.write('<html><body>\n')     # prepping the html page by declaring html setting up the body
  
  for img in img_urls:      
      urllib.urlretrieve(img, dest_dir + '\img' + str(img_urls.index(img)))  # retrieving the url and downloading to specified location     
      print 'retrieving... ' + img  # print message to let user know that the system is active
      index.write('<img src="img' + str(img_urls.index(img)) + '">')  # writing the images to html in order to build a whole picture
 
  index.write('\n</body></html>\n')  # finishing the index by close the body and html nodes
  index.close()  # closing the index file
  print 'creating index.html'  # letting the user know the index.html file was created
  
    
def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
