#!/usr/bin/python
import sys
import glob
import os

# Get the directory name
if sys.platform == 'darwin':
    hdir = os.path.expanduser('~')  # /Users/sirl0fty/Documents/Projects/Python Projects/Exercise 10/ex10_starter.py
else:
    hdir = os.environ['HOME']  # /Users/sirl0fty

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames

print('Path Name:')
for name in glob.glob(hdir):  # shows the path of home hdir
    print(name)

print('\nNamed with wildcard *:')  # lists out the file names within hdir directory
for name in glob.glob(pattern):
    print(name)

# TODO: use os.path.getsize to find each file's size
print("File Sizes")
for filesize in glob.glob(pattern):
    if os.path.getsize(filesize) != 0:  # TODO: Add a test to only display files that do not have a size of zero
        print(os.path.getsize(filesize)) #can't figure out how to join pattern and filesize together
    print("")

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

print("Filename without path")
for filename in glob.glob(pattern):
    print(os.path.basename(filename))
print("")
