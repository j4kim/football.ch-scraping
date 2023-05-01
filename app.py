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
        "/home/j4kim/.virtualenvs/footballenv/bin/scrapy",
        "runspider", "/home/j4kim/football/matches_spider.py",
        "-O", "/home/j4kim/football/matches.json",
        "-a", "club=907",
        "-a", "team=34040",
    ]
    subprocess.run(command, check=True)
    with open("/home/j4kim/football/matches.json") as f:
        return f.read()
