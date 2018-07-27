from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    title = "home"
    return render_template('index.html', user=user, title=title)