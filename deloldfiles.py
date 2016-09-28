#!/usr/bin/python

import os, sys, time
from subprocess import call

def get_file_directory(file):
    return os.path.dirname(os.path.abspath(file))

now = time.time()
cutoff = now - (60)

files = os.listdir(os.path.join(get_file_directory(__file__), "files"))
file_path = os.path.join(get_file_directory(__file__), "files/")
for xfile in files:
    if os.path.isfile(str(file_path) + xfile):
        t = os.stat(str(file_path) + xfile)
        c = t.st_ctime

        # delete file if older than 1 minute
        if c < cutoff:
            os.remove(str(file_path) + xfile)
