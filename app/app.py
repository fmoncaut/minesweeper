import sys

from flask import Flask, jsonify, render_template, request

sys.path.insert(0, ".")
from src.minesweeper import Minesweeper

app = Flask(__name__)
game = Minesweeper(8, 8, 10)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/board")
def board():
    return jsonify({"board": game.get_board(), "winner": game.is_winner()})


@app.route("/reveal", methods=["POST"])
def reveal():
    data = request.json
    result = game.reveal(data["row"], data["col"])
    return jsonify(
        {"result": result, "board": game.get_board(), "winner": game.is_winner()}
    )


@app.route("/restart", methods=["POST"])
def restart():
    game.restart()
    return jsonify({"board": game.get_board()})


if __name__ == "__main__":
    app.run(debug=True)
