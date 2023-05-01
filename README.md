# football

Data scraping from football.ch

## Install

    python -m venv .venv

    ./.venv/bin/activate

    pip install -r ./requirements.txt

## Run spider

    scrapy runspider matches_spider.py -a club=907 -a team=34040 -O matches.json

## Run Flask app

    cp config.example.py config.py

    flask run --debug
