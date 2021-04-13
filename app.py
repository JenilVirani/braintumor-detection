
from flask import Flask, request

app = Flask(__name__)

@app.route("https://braintumor-detection.herokuapp.com/")
def demo():
    return "<html><body><h1>Hello World</h1></body></html>"



app.run(port=8080)
