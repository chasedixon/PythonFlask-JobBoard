from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/jobs")
def index():
    render_template('index.html')

