import scrapy

class Spider(scrapy.Spider):
    name = 'matches'

    def start_requests(self):
        club = self.club
        team = self.team
        url = f'https://matchcenter-anf.football.ch/?v={club}&t={team}&a=pt'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for matches in response.css('.row.spiel'):
            yield {
                'date': matches.css('.date span::text').get(),
                'time': ''.join(matches.css('.date::text').getall()),
                'teamA': ''.join(matches.css('.teamA *::text').getall()),
                'teamB': ''.join(matches.css('.teamB *::text').getall()),
                'goalsA': matches.css('.torA::text').get(),
                'goalsB': matches.css('.torB::text').get(),
                'sppStatusText': matches.css('.sppStatusText::text').get(),
            }