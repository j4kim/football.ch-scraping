from flask import Flask
import subprocess
from flask_caching import Cache
from flask_cors import CORS
import config

app = Flask(__name__)
cache = Cache(app, config={
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 60 * 60 # 1 hour
})
CORS(app)

@app.route("/")
def index():
    return "Hello"

@app.route("/matches")
@cache.cached()
def matches():
    command = [
        config.scrapy,
        "runspider", config.matches_spider,
        "-O", config.matches_file,
        "-a", f"club={config.club}",
        "-a", f"team={config.team}",
    ]
    subprocess.run(command, check=True)
    with open(config.matches_file) as f:
        return f.read()
