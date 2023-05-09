from flask import Flask
from flask_cors import CORS
import bot

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Hello"

@app.route("/matches")
def matches():
    return bot.get()

@app.route("/matches/fresh")
def freshMatches():
    return bot.run_and_get()
