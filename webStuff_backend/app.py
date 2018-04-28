from flask import Flask, render_template, request
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import sys
import os
import PIL.ImageOps
from PIL import Image, ImageFilter
from werkzeug import secure_filename
# from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class


sys.path.append(os.path.abspath('./model'))
from load import *

#init flask app
app = Flask(__name__)

global model, graph
model, graph = init()


def convertImage(argv):
    print("<NITYAM>...>!!!...", argv)
    im = Image.open(argv).convert('L')
    im = im.resize((28, 28), Image.ANTIALIAS)
    im = PIL.ImageOps.invert(im)
    print("<NITYAM>...>!!!...", type(im))
    return list(im.getdata())

def imageProcess(imgData):
    pic1 = convertImage(imgData)
    pic1 = np.array(pic1)
    pic1 = pic1.astype(np.float32)
    pic1 = pic1.reshape(1, 28, 28, 1)
    pic1 = pic1.astype('float32')
    pic1 /= 255
    return pic1;

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload')
def upload_file():
    return render_template('index.html')

@app.route('/uploader', methods = ['GET','POST'])
def uploader():
    print ("testing the upload function")
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename("digit.png"))
        pic = imageProcess("digit.png")
        print("<NITYAM>...>!!!...UPLOADER", type(pic))

        with graph.as_default():
            out = model.predict_classes(pic)
            print("NITYAM SAYS>>>>>....>>>...>>>..", out)
            return 'done'

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port = port)
