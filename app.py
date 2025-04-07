import flask
from flask import render_template

app = flask.Flask(__name__)

players = [
    {"name": "Zara", "score": 67},
    {"name": "Liam", "score": 89},
    {"name": "Emma", "score": 95},
    {"name": "Noah", "score": 72},
    {"name": "Olivia", "score": 88}
]

@app.route("/sortedByNameASC")
def sort_name():
    sorted_players = sorted(players, key=lambda x:x["name"])
    return render_template("display.html", players=sorted_players)

@app.route("/sortedByScoreDESC")
def sort_score():
    sorted_players = sorted(players, key=lambda x:x["score"], reverse=True)
    return render_template("display.html", players=sorted_players)


if __name__ == "__main__":
    app.run()
