# Football.ch scraping

Data scraping from football.ch using [scrapy](https://scrapy.org/) and API to extract data on demand.

## Install

    python -m venv .venv

    ./.venv/bin/activate

    pip install -r ./requirements.txt

    cp config.example.py config.py

## Run spider

    scrapy runspider matches_spider.py -a asso=anf -a club=907 -a team=34040 -O matches.json

## Run Flask app

    flask run --debug
