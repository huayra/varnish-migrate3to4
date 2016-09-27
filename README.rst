Varnish-Migrate3to4
-------------------

A Simple PoC Web App for VCL migration

**This is a WIP**
-----------------

To test it:

- Clone repository

  cd varnish-migrate3to4

- Run server.py

  $ python server.py

- Open browser to view page

  http://0.0.0.0:5001/

- Upload a vcl file

- Click on Convert

- Converted file is stored with extension `.v4`

- Converted folder to tarball with tar


**TARGET**

To directly convert uploaded file to v4 and convert to tarball
then display tarball for download


Requirements
............

- Flask

  $ pip install Flask

- Tar

  $ apt-get install tar

Resources
.........

**File uploader Cloned from simple-file-service**
A simple file uploader and downloader service in python flask.
https://github.com/ihopeit/simple-file-service

visit http://localhost:5001 to upload files, you can visit uploaded files on the same page.

**Varnish Migrator from varnish3to4**
https://github.com/fgsch/varnish3to4
