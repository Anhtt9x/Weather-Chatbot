from flask import Flask, render_template, request, make_response
import os , json
from flask_cors import CORS, cross_origin
from weather_data import WeatherData
from dotenv import load_dotenv
load_dotenv()

own_key=os.getenv('OWN_KEY')

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome"


@app.route("/webhook",methods=["POST"])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")

    print(json.dumps(req))
    res = object.processRequest(req)

    res = json.dumps(res)
    print(res)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'

    return r



if __name__ == "__main__":
    object = WeatherData(own_key)
    app.run(host="0.0.0.0", port=8000)  # run with debug mode on