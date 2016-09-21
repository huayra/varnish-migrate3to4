#!/usr/bin/env python

import subprocess
import os

for filename in os.listdir('/home/syeda/vagrant/varnish-migrate3to4/files'):
    if filename.endswith(".vcl"):
        print filename
        outfile_name = '{0}{1}'.format(filename,".v4")
        print outfile_name
        call_cmd = 'python varnish3to4 -o {0} {1}'.format(outfile_name, filename)
        print call_cmd
        subprocess.call(call_cmd, shell=True)
