from flask import Flask

app = Flask(__helloworld__)

@app.route("/")
def hello_world():
    return "<p>In the Flesh?</p>"