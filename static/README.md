# Football.ch scraping

## Get matches calendar

Path to get matches calendar for a specific team: `/matches/{association}/{club}/{team}`

Example:

[/matches/anf/907/34040](/matches/anf/907/34040 ":ignore")

Will extract data from:

https://matchcenter-anf.football.ch/?v=907&t=34040&a=pt

## Refresh data

By default the API will return a saved version of the extracted data.

To force scraping and get fresh data, you can add `?fresh=1` to the URL.
