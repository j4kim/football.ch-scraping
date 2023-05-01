from flask import Flask
import subprocess
from flask_caching import Cache


app = Flask(__name__)
cache = Cache(app, config={
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 60 * 60 # 1 hour
})

@app.route("/matches")
@cache.cached()
def matches():
    command = [
        "scrapy", "runspider", "matches_spider.py",
        "-O", "matches.json",
        "-a", "club=907",
        "-a", "team=34040",
    ]
    return subprocess.getoutput(" ".join(command))
    with open("matches.json") as f:
        return f.read()