import subprocess
import config
from os.path import getmtime
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

    def get(self):
        with open(self.filename) as f:
            return {
                "matches": json.load(f),
                "time": getmtime(self.filename),
            }

    def run_and_get(self):
        self.run()
        return self.get()


if __name__ == "__main__":
    bot = Bot("anf", 907, 34040)
    bot.run()
