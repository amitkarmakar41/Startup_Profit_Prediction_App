import numpy as np
import pickle
from flask import Flask, render_template , request, redirect, jsonify

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)