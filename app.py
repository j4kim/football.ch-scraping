from flask import Flask, request
from flask_cors import CORS
from bot import Bot

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Hello"


@app.route("/matches/<asso>/<int:club>/<int:team>")
def matches(asso, club, team):
    fresh = request.args.get("fresh") == "1"
    bot = Bot(asso, club, team)
    return bot.get(fresh)
