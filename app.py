from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to my API!", "status": "running"}), 200

@app.route("/square", methods=["GET"])
def square():
    """Returns the square of a number"""
    try:
        num = float(request.args.get("number", 0))
        return jsonify({"number": num, "square": num**2}), 200
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)