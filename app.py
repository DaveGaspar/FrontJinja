from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

@app.route("/")
def home():
    point = Point(5,7)
    data = json.loads(json.dumps(point.__dict__))
    return render_template("index.html", data=data)
