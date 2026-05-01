from flask import Flask, jsonify
from main import scrape_jobs

app = Flask(__name__)

@app.route("/jobs", methods=["GET"])
def jobs():
    try:
        data = scrape_jobs()     # run your selenium scraper
        return jsonify(data)     # send JSON to Flutter
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
