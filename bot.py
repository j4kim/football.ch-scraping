import subprocess
import config

def run():
    command = [
        config.scrapy,
        "runspider", config.matches_spider,
        "-O", config.matches_file,
        "-a", f"club={config.club}",
        "-a", f"team={config.team}",
    ]
    subprocess.run(command, check=True)

def get():
    with open(config.matches_file) as f:
        return f.read()

def run_and_get():
    run()
    return get()