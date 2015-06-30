#!/usr/bin/env python2
from flask import Flask, request, render_template, send_file
import fnmatch
import os

from config import *

app = Flask(__name__)
app.use_x_sendfile = True

if not PATH[-1] in ["\\", "/"]:
  print "Path should have a / (or \\) at the end. Fixing, but you should update the config file. You'll continue to see this warning until you do."
  PATH = PATH + "/"

mp3s = []
for root, dirnames, filenames in os.walk(PATH):
  for filename in fnmatch.filter(filenames, '*.mp3'):
    mp3s.append(os.path.join(root, filename).replace(PATH, ""))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if path and ".mp3" in path:
        return send_file(PATH + path)
    if path == "folder.jpg":
        try:
            return send_file(PATH + "folder.jpg")
        except:
            return "", 404
    return render_template('index.html', mp3s=mp3s)

if __name__ == "__main__":
    app.run(port=56344)
