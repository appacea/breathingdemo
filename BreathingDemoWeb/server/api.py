from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from detector.processor import getCustomPulseApp
import numpy as np
import cv2
import calendar
import time
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
args = {
    "serial":None,
    "baud":None,
    "udp":None
}
pulse = getCustomPulseApp(args)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


@socketio.on('frame')
def handle_frame(b64):
#    print('data: ' + str(b64))

#    file = 'image'+time.strftime("%H%M%S")+'.png'
#    with open(file,"wb") as fh:
#        fh.write(base64.decodebytes(b64))
    img = base64.b64decode(b64)
    img = np.array(list(img))
    img_array = np.array(img, dtype = np.uint8)
    frame = cv2.imdecode(img_array, 1)
    pulse.process(frame)

@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my_response',
         {'data': 'bugges'})
    print('received json: ' + str(json))

if __name__ == '__main__':
    socketio.run(app)

