#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

from flask import Flask
from flask import render_template, redirect, request, url_for, send_file
from werkzeug.utils import secure_filename

from PIL import Image
from image_process import process_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# start web app
def start(host="localhost", port=80, debug=True):
    try:
        app.run(host=host, port=port, debug=debug)
    except Exception as err:
        print("[error]", str(err))

# routes
@app.route('/')
def index():
    return render_template(r'index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print('[*] File uploaded successfully')
    else:
        print("[!] No file uploaded")
        return 'No file uploaded'
    
    # Process the image
    img = Image.open(file)
    processed_img = process_image(img) # Your image processing code here

    # Save the processed image to a temporary file
    temp_file = 'temp.png'
    processed_img.save(temp_file)

    # Send the processed image file to the user's browser
    return send_file(temp_file, mimetype='image/png')





# main
if __name__ == "__main__":
    # run on defaults (host:port)
    start(debug=True)
