import subprocess
import config
from os.path import getmtime, isfile
import json


class Bot:
    def __init__(self, asso, club, team):
        self.asso = asso
        self.club = club
        self.team = team
        self.filename = f"matches/{asso}/{club}/{team}.json"

    def run(self):
        command = [
            config.scrapy,
            "runspider",
            config.matches_spider,
            "-O",
            self.filename,
            "-a",
            f"club={self.club}",
            "-a",
            f"team={self.team}",
        ]
        subprocess.run(command, check=True)

    def get(self, fresh=False):
        if fresh or not isfile(self.filename):
            self.run()
        with open(self.filename) as f:
            return {
                "matches": json.load(f),
                "time": getmtime(self.filename),
            }


if __name__ == "__main__":
    bot = Bot("anf", 907, 34040)
    bot.run()
