# app_flask.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "World")
    return jsonify(message=f"Hello, {name} from Flask!")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

 ##run with -> python app_flask.py

