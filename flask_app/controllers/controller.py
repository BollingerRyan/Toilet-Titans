from flask import render_template
from flask_app import app

@app.route('/')
def show_home_page():
    return render_template('index.html')

@app.route('/privacy_policy')
def show_privacy_policy():
    return render_template('privacy_policy.html')