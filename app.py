from flask import Flask, request, jsonify, render_template
from dream_decoder import DreamDecoder
import csv

app = Flask(__name__)
decoder = DreamDecoder()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/decode", methods=["POST"])
def decode_dream():
    data = request.get_json()
    dream = data.get("dream", "")
    if not dream.strip():
        return jsonify({"error": "No dream text provided."}), 400

    results = decoder.decode(dream)
    return jsonify({"dream": dream, "interpretations": results})

@app.route("/feedback", methods=["POST"])
def save_feedback():
    data = request.get_json()
    dream = data.get("dream", "")
    symbol = data.get("symbol", "")
    feedback = data.get("feedback", "")

    with open("feedback_log.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([dream, symbol, feedback])

    return jsonify({"message": "Feedback saved"}), 200

if __name__ == "__main__":
    app.run(debug=True)
