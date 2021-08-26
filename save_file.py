#!/usr/bin/python3
import cgi, sys, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

sys.path.insert(0, os.getcwd())

message = None

if 'filename' in form:
    fileitem = form['filename']
    fn = os.path.basename(fileitem.filename)
    open('/home/arq/' + fn, 'wb').write(fileitem.file.read())
    message = 'O arquivo "' + fn + '" foi upado'
