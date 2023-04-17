import scrapy

class Spider(scrapy.Spider):
    name = 'matches'
    start_urls = ['https://matchcenter-anf.football.ch/default.aspx?lng=2&cxxlnus=1&v=907&t=34040&ls=20261&sg=58387&a=pt&']

    def parse(self, response):
        for matches in response.css('.row.spiel'):
            yield {
                'date': matches.css('.date span::text').get(),
                'time': ''.join(matches.css('.date::text').getall()).strip(),
                'teamA': ''.join(matches.css('.teamA *::text').getall()).strip(),
                'teamB': ''.join(matches.css('.teamB *::text').getall()).strip(),
                'goalsA': matches.css('.torA::text').get().strip(),
                'goalsB': matches.css('.torB::text').get().strip(),
                'sppStatusText': matches.css('.sppStatusText::text').get(),
            }