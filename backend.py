from flask import Flask, render_template, Response, request
from extraction import SampleItems
from importlib import import_module
import os


#------
from werkzeug import secure_filename
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import sys
import os
import PIL.ImageOps
from PIL import Image, ImageFilter

sys.path.append(os.path.abspath('./model'))
from load import *

global model, graph
model, graph = init()
#---

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    flash('Please have a camera and enable permissions!')
    # from camera import Camera

app = Flask(__name__)


SampleItems = SampleItems()



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

# Route for Home page
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/picture")
def pic():
    return render_template('pic.html')

@app.route('/image', methods=['POST'])
def image():
    i = request.files['image']  # get the image
    f = ('%s.png' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))

    return Response("%s saved" % f)

# Adding other route, Getting started
@app.route('/getStarted')
def getStarted():
	return render_template('getStarted.html', sample = SampleItems)

# For Getting Video
def generate_stock_table():
    yield render_template('stock_header.html')
    for stock in Stock.query.all():
        yield render_template('stock_row.html', stock=stock)
    yield render_template('stock_footer.html')

# For scan camera
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/prediction_page', methods = ['GET','POST'])
def prediction_page():
    print ("testing the upload function")
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename("digit.png"))
        pic = imageProcess("digit.png")
        print("<NITYAM>...>!!!...UPLOADER", type(pic))

        with graph.as_default():
            out = model.predict_classes(pic)
            print("NITYAM SAYS>>>>>....>>>...>>>..", type(out[0]))
            str1 = ''.join(str(e) for e in out)
            print(str1)
            return str1




if __name__ == '__main__':
	# app.run(debug = True)
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port = port, debug = True)
