from flask import Flask, Response, render_template, request
import time

app = Flask(__name__)

frame = None

@app.route('/upload', methods=['PUT'])
def upload():
    global frame
    
    frame = request.data
    
    return "OK"

def gen():
    while True:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n'
               b'\r\n' + frame + b'\r\n')
        time.sleep(0.04)

        
@app.route('/video')
def video():
    if frame:
        return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return ""
    
@app.route("/home")
def home():
    return render_template('index.html')
