from flask import Flask, jsonify
from rick_morty_client import RickMortyClient

app = Flask(__name__)

@app.route("/")
def home():
    client = RickMortyClient()
    data = client.get_characters()

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)