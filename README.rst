Varnish-Migrate3to4
-------------------

A Simple PoC Web App for VCL migration

**This is a WIP**
-----------------

**File uploader Cloned from simple-file-service**
A simple file uploader and downloader service in python flask.
https://github.com/ihopeit/simple-file-service

visit http://localhost:5001 to upload files, you can visit uploaded files on the same page.

**Varnish Migrator from varnish3to4**
https://github.com/fgsch/varnish3to4

Add test.py to crontab with:

crontab -e

*/1 * * * * /usr/bin/python test.py
