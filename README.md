# Football.ch scraping

Data scraping and API to extract data from [football.ch](https://football.ch) for regional associations (ANF, etc.).

## Install

    python -m venv .venv

    source ./.venv/bin/activate

    pip install -r ./requirements.txt

    cp config.example.py config.py

## Run spider

    scrapy runspider matches_spider.py -a asso=anf -a club=907 -a team=34040 -O matches.json

## Run Flask app

    flask run --debug

## Production setup

The app is deployed on a Jelastic cloud hosted by Infomaniak, here: https://football-ch-scraping.jcloud.ik-server.com.

A contab entry is added to keep data up to date for fclesbrenets.ch:

    @hourly cd /var/www/webroot/ROOT && python bot.py anf 907 34040 > joblog 2>&1
