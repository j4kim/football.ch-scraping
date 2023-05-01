# football

Data scraping from football.ch

## Install

    python -m venv .venv

    ./.venv/bin/activate

    pip install -r ./requirements.txt

## Run spider

    scrapy runspider spider.py -O matches.json

## Run Flask app

    flask run