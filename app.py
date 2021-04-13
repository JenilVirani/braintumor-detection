
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def demo():
    return "HELLO"



app.run(port=7890, threaded=True, debug=True)
