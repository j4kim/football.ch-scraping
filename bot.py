import subprocess
import config
from os.path import getmtime
import json


class Bot:
    def __init__(self, club, team):
        self.club = club
        self.team = team

    def run(self):
        command = [
            config.scrapy,
            "runspider",
            config.matches_spider,
            "-O",
            config.matches_file,
            "-a",
            f"club={self.club}",
            "-a",
            f"team={self.team}",
        ]
        subprocess.run(command, check=True)

    def get():
        with open(config.matches_file) as f:
            return {
                "matches": json.load(f),
                "time": getmtime(config.matches_file),
            }

    def run_and_get(self):
        self.run()
        return self.get()


if __name__ == "__main__":
    bot = Bot(config.club, config.team)
    bot.run()
