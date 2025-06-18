from flask import Flask, render_template, request, jsonify
from citylist import cities
from scrape import get_weather_info

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def initiator():
    return render_template("index.html", cities=cities)

@app.route("/api", methods=["POST"])
def api():
    city = request.get_json()["city"]
    print(request.get_json())
    citydata = get_weather_info(city)

    return jsonify(citydata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)