from flask import Flask, current_app
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

@app.route('/')
def site():
    return current_app.send_static_file('client.html')


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


@socketio.on('frame')
def handle_frame(b64):
#    print('data: ' + str(b64))

#    file = 'image'+time.strftime("%H%M%S")+'.jpg'
#    with open(file,"wb") as fh:
#        fh.write(base64.b64decode(b64))
    try:
        img = base64.b64decode(b64)
        img = np.array(list(img))
        img_array = np.array(img, dtype = np.uint8)
        frame = cv2.imdecode(img_array, 1)
        imout = pulse.process(frame)
        retval, buf = cv2.imencode('.jpg',imout)
        b64out = base64.b64encode(buf)
      #  file = 'imageout-'+time.strftime("%H%M%S")+'.jpg'
      #  with open(file,"wb") as fh:
      #      fh.write(base64.b64decode(b64out))
      #  print(b64out)
        emit('response',b64out.decode('utf-8'))
    except Exception as e:
        print(e)
        
@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my_response',
         {'data': 'bugges'})
    print('received json: ' + str(json))

if __name__ == '__main__':
  #  socketio.run(app,host='0.0.0.0',port=3001)
    socketio.run(app,host='0.0.0.0')
    app.run()
