import scrapy

def clean(text):
    if not text: return None
    text = text.strip()
    if text.isnumeric(): return int(text)
    return text

class Spider(scrapy.Spider):
    name = 'matches'

    def start_requests(self):
        club = self.club
        team = self.team
        url = f'https://matchcenter-anf.football.ch/?v={club}&t={team}&a=pt'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for matches in response.css('.row.spiel'):
            fdate = matches.css('.date span::text').get()
            yield {
                'fdate': fdate,
                # transform fdate from "Sa DD.MM.YYYY" to "YYYY-MM-DD"
                'date': f'{fdate[9:13]}-{fdate[6:8]}-{fdate[3:5]}',
                'time': clean(''.join(matches.css('.date::text').getall())),
                'teamA': clean(''.join(matches.css('.teamA *::text').getall())),
                'teamB': clean(''.join(matches.css('.teamB *::text').getall())),
                'goalsA': clean(matches.css('.torA::text').get()),
                'goalsB': clean(matches.css('.torB::text').get()),
                'sppStatusText': matches.css('.sppStatusText::text').get(),
            }