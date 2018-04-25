from flask import Flask, render_template, Response
from extraction import SampleItems
from importlib import import_module
import os

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    flash('Please have a camera and enable permissions!')
    # from camera import Camera

app = Flask(__name__)


SampleItems = SampleItems()

# Route for Home page
@app.route("/")
def index():
    return render_template('index.html')

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





if __name__ == '__main__':
	app.run(debug = True)