# simple file uploader that converts vcl3 to vcl4
# returns a number of files: .vcl4, changes made .dff and a tar with all the files

import os
import urllib
import cgi
from flask import Flask, request, redirect, url_for, send_from_directory
from secure_file import secure_filename

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

BASE_DIR = os.path.dirname(__file__)

print ("dir:%s" % BASE_DIR)

os.system('mkdir -p files')

UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = set(['vcl'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def list_directory(path):
        """Helper to produce a directory listing (absent index.html).

        Return value is either a file object, or None (indicating an
        error).  In either case, the headers are sent, making the
        interface the same as for send_head().

        """
        try:
            list = os.listdir(path)
        except os.error:
            return "No permission to list directory"
        list.sort(key=lambda a: a.lower())
        f = StringIO()
        displaypath = cgi.escape(urllib.unquote(path))
        f.write("<body><h4>Your VCL tarball:</h4>")
        f.write("<form ENCTYPE=\"multipart/form-data\" method=\"post\">")

        for name in list:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                displayname = name + "@"
                # Note: a link to a directory displays with @ and links with /
            f.write('<a href="uploads/%s">%s</a>\n'
                    % (urllib.quote(linkname), cgi.escape(displayname)))
        f.write("\n<hr>\n</body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        #self.send_response(200)
        #self.send_header("Content-type", "text/html")
        #self.send_header("Content-Length", str(length))
        #self.end_headers()
        return f


@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(BASE_DIR, UPLOAD_FOLDER)
    return send_from_directory(directory=uploads, filename=filename)

@app.route("/", methods=['GET', 'POST'])
def index():
    import subprocess
    import os
    import time
#    import tarfile
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            print('filename:%s' % file.filename)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            #start here
            dir_abs=os.path.abspath('.')
            path=os.path.join(dir_abs, 'files/')
            dir_file=os.path.join(dir_abs, 'files')
            os.system('mkdir -p vcl_tar')
            path_tar=os.path.join(dir_abs, 'vcl_tar/')
            dir_tar=os.path.join(dir_abs, 'vcl_tar')
            timestr = time.strftime("%Y%m%d-%H%M%S")

            for filename in os.listdir(dir_file):
                if filename.endswith(".vcl"):
                    outfile_name = '{0}{1}'.format(filename,".v4")
                    call_cmd = 'python varnish3to4 -o {0}{1} {2}{3}'.format(path_tar, outfile_name, path, filename)
                    subprocess.call(call_cmd, shell=True)
                    diff_out = '{0}{1}'.format(filename,".diff")
                    os.system('diff -u {0}{1} {2}{3} >> {4}{5}'.format(path_tar, outfile_name, path, filename, path_tar, diff_out))
                    os.system('mv {0}{1} {2}{3}'.format(path, filename, path_tar, filename))
                    os.system('tar -zcvf {0}{1}{2} -C {3} .'.format(path, timestr, ".vcl.tar.gz", dir_tar))
                    os.system('rm -rf {0}'.format(dir_tar))
                # removes last tar file in folder
                else:
                    os.remove(str(path) + filename)

            return redirect(url_for('index'))
    return """
    <!doctype html>
    <title>Varnish3to4</title>

    <h1>Varnish3to4 Migrator</h1>

    Migrate your varnish 3 codes on the fly.

    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Convert>
    </form>
    %s
    """ % "<br>".join(list_directory(app.config['UPLOAD_FOLDER']))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
