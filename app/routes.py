from app import app
from flask import render_template

@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sim')
def sim():
    return render_template('sim.html')
