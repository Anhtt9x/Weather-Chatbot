from flask import Flask, render_template, request, make_response
import os , json
from flask_cors import CORS, cross_origin



app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome"









if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)  # run with debug mode on