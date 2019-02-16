import os
from importlib import import_module
import functools

from flask import Flask, render_template

app = Flask(__name__, instance_relative_config=True)

@app.route("/")
def hello():
    return 'Welcome, please choose the path'

def get_visual_files(species_name):
	return [os.path.join('js','.'.join([species_name,'js']))]
	
@app.route("/<path:filename>")
def homepage(filename):
	parent_name = filename
	return render_template('detail.html', js_files=get_visual_files(parent_name))

def get_json(filename):
    my_module = import_module('.fishes', package='app.apis')
    return my_module.main()

@app.route('/api/<path:filename>')
def api(filename):
    return get_json(filename)