import os
import sys
from werkzeug.utils import secure_filename
from flask import Flask, render_template, flash, request, redirect, url_for
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
app.debug = True
run_with_ngrok(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def choose_mode():
    if request.form.get("generate"):
        return render_template('generate.html', data=[])
    elif request.form.get("assess"):
        return render_template('assess.html', data=[])
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()