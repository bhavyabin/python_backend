from flask import Flask, render_template,  request, jsonify
from duh import cities
from scrape import get_weather_info

app = Flask(__name__)

@app.route("/")
def initiator():
    return render_template("index.html", cities=cities)

@app.route("/api", methods=["POST"])
def api():
    city = request.get_json()["city"]
    citydata = get_weather_info(city)

    return jsonify(citydata)