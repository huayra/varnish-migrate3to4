import os
import subprocess

#file='/home/syeda/vagrant/varnish-migrate3to4/files/testvcl.vcl'
subprocess.call(["python varnish3to4 -o testvclv4 testvcl.vcl"], shell=True)

#os.system('python varnish3to4 -o testvclv4 file')
