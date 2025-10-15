from flask import Flask, jsonify, request, send_from_directory
from .game import Game

app = Flask(__name__, static_folder="static", static_url_path="/static")

# single shared game instance (change to per-session if needed)
game = Game()

def state_json():
    return {
        "board": game.board,
        "score": game.score,
        "game_over": game.is_game_over(),
        "won": game.won
    }

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/state", methods=["GET"])
def get_state():
    return jsonify(state_json())

@app.route("/api/move", methods=["POST"])
def move():
    data = request.get_json() or {}
    direction = data.get("direction", "")
    game.move(direction)
    return jsonify(state_json())

@app.route("/api/reset", methods=["POST"])
def reset():
    game.reset()
    return jsonify(state_json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
