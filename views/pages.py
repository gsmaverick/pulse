from flask import render_template

import api

def index():
    return render_template('index.html')

def about():
    return render_template('about.html')

def help():
    return render_template('help.html')

def app():
    return render_template('app.html')