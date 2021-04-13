
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def demo():

    return "<html><body><h1>Hello World</h1></body></html>"



app.run(port=7890, threaded=True, debug=True)
