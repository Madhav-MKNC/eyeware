#!/usr/bin/python
# -*- coding: UTF-8 -*-

# web app

from flask import Flask
from flask import render_template, redirect, request, url_for, send_file
from PIL import Image

app = Flask(__name__)

# start web app
def start(host="localhost", port=80, debug=True):
    try:
        app.run(host=host, port=port, debug=debug)
    except Exception as err:
        print("[error]", str(err))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded image file
    img_file = request.files['image']

    # Process the image
    img = Image.open(img_file)
    processed_img = 1# Your image processing code here

    # Save the processed image to a temporary file
    temp_file = 'temp.png'
    processed_img.save(temp_file)

    # Send the processed image file to the user's browser
    return send_file(temp_file, mimetype='image/png')




if __name__ == "__main__":
    # run on defaults (host:port)
    app.run(debug=True)
