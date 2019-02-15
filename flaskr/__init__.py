import os
from importlib import import_module

from flask import Flask, render_template

app = Flask(__name__, instance_relative_config=True)

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route("/hai")
def hello123():
    return render_template('detail.html')

def get_json(filename):
    category_path = filename.split('/')
    my_module = import_module('.' + '.'.join(category_path), package='apis')
    return my_module.main()

@app.route('/api/<path:filename>')
def api(filename):
    return get_json(filename)