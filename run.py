#!/usr/bin/env python2
from flask import Flask, request, render_template, send_file
import fnmatch
import os

app = Flask(__name__)
app.use_x_sendfile = True

PATH = "/home/sites/joco/"
mp3s = []
for root, dirnames, filenames in os.walk(PATH):
  for filename in fnmatch.filter(filenames, '*.mp3'):
    mp3s.append(os.path.join(root, filename).replace(PATH, ""))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if path and ".mp3" in path:
        return send_file(PATH + path)
    global mp3s
    return render_template('index.html', mp3s=mp3s)

if __name__ == "__main__":
    app.run(port=56344)
