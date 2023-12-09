# Football.ch scraping

Data scraping and API to extract data from [football.ch](https://football.ch) for regional associations (ANF, etc.).

## Install

    python -m venv .venv

    source ./.venv/bin/activate

    pip install -r ./requirements.txt

    cp config.example.py config.py

## Run

Scraping is performed using [Scrapy](https://docs.scrapy.org/).

The `matches_spider.py` scripts retrieves calendar for a certain team of a cerain club in a certain association (anf, acvf, etc.).

The club and the team are represented by args `v` and `t` on football.ch.

Example:

    scrapy runspider matches_spider.py -a asso=anf -a club=907 -a team=34040 -O matches.json

Will extract data from https://matchcenter-anf.football.ch/?v=907&t=34040&a=pt.

The script `bot.py` runs `matches_spider.py` and saves the result in `matches` directory.

## Run Flask app

    flask run --debug

The app offers an API to get extracted data.

## Production setup

The project is deployed on a Jelastic cloud hosted by Infomaniak, here: https://football-ch-scraping.jcloud.ik-server.com.

A contab entry is added to keep data up to date for fclesbrenets.ch:

    @hourly cd /var/www/webroot/ROOT && python bot.py anf 907 34040 > joblog 2>&1
