from flask import Flask
import subprocess
from flask_caching import Cache


app = Flask(__name__)
cache = Cache(app, config={
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 60 * 60 # 1 hour
})

@app.route("/")
@cache.cached()
def hello_world():
    subprocess.check_output(["scrapy", "runspider", "spider.py", "-O", "matches.json"])
    with open("matches.json") as f:
        return f.read()