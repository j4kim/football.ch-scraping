from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def hello_world():
    subprocess.check_output(["scrapy", "runspider", "spider.py", "-O", "matches.json"])
    with open("matches.json") as f:
        return f.read()