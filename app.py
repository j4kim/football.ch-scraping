from flask import Flask
import subprocess
from flask_cors import CORS
import config

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Hello"

@app.route("/matches/fresh")
def freshMatches(self):
    command = [
        config.scrapy,
        "runspider", config.matches_spider,
        "-O", config.matches_file,
        "-a", f"club={config.club}",
        "-a", f"team={config.team}",
    ]
    subprocess.run(command, check=True)
    return self.cachedMatches()

@app.route("/matches/cached")
def cachedMatches():
    with open(config.matches_file) as f:
        return f.read()
