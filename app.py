from flask import Flask, render_template, request, jsonify
import requests
import tensorflow as tf
import numpy as np
import json
import requests
app = Flask(__name__) 
@app.route('/')
def home():
    return render_template('home.html')  


def pre_process(img):
    img = tf.keras.preprocessing.image.load_img(img, target_size=(96, 96))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img 
def prediction():
    img='image path'
    img=pre_process(img)
    url='https://us-central1-global-snow-372118.cloudfunctions.net/crapguru_func_v1'
    payload = json.dumps({"instances": img.tolist()})
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=payload, headers=headers)
    result = response.json()
    predictions = result["predictions"]
    print(predictions) 

@app.route("/info")
def info():
    return render_template('info.html')  
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)  


