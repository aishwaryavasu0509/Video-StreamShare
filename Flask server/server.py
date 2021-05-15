from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        #print(uploaded_file.filename)
        uploaded_file.save(uploaded_file.filename)
        mp3_f = open(uploaded_file.filename, 'rb')
        vfiles = {'messageFile': mp3_f}
        #Passing the video as frame to the Django server running on port 9000
        r = requests.post("http://127.0.0.1:9000", files=vfiles)
        print(r.text)
    return redirect(url_for('index'))


app.run(host="localhost", port=8000, debug=True)