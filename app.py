from flask import Flask, render_template, request, jsonify
from scrape import get_weather_info,get_weather_info_using_station_id
from citylist import cities
import json

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def initiator():
    return render_template("index.html", cities=cities)

@app.route("/api", methods=["POST"])
def api():
    with open("station_ids.json","r") as f:
        return jsonify(json.load(f))

@app.route("/api/id", methods=["POST"])
def api_using_id():
    station_id = request.get_json()["station_id"]
    return jsonify(get_weather_info_using_station_id(station_id))

@app.route("/api/name", methods=["POST"])
def api_using_station_name():
    station_name = request.get_json()["station"]
    return jsonify(get_weather_info(station_name))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)