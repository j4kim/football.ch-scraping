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
    subprocess.check_output(["scrapy", "runspider", "matches_spider.py", "-O", "matches.json"])
    with open("matches.json") as f:
        return f.read()