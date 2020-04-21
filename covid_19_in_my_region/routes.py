from covid_19_in_my_region import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')
