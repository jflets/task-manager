from flask import render_template
from taskmanager import app, db


@app.route('/')
def index():
    return render_template('base.html')
