from flask import Flask, render_template, request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        print(request.form['search'])
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    manager.run()
