from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html', title='Home Page')

@app.route('/about')
def about():
    return render_template('about.html', title='About Page')
