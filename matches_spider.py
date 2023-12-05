import scrapy


def clean(text):
    if not text:
        return None
    text = text.strip()
    if text.isnumeric():
        return int(text)
    return text


class Spider(scrapy.Spider):
    name = "matches"

    def start_requests(self):
        club = self.club
        team = self.team
        url = f"https://matchcenter-anf.football.ch/?v={club}&t={team}&a=pt"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for match in response.css(".row.spiel"):
            fdate = match.css(".date span::text").get()
            # transform fdate from "Sa DD.MM.YYYY" to "YYYY-MM-DD"
            date = f"{fdate[9:13]}-{fdate[6:8]}-{fdate[3:5]}"
            time = clean("".join(match.css(".date::text").getall()))
            datetime = f"{date} {time}"
            yield {
                "fdate": fdate,
                "date": date,
                "time": time,
                "datetime": datetime,
                "teamA": clean("".join(match.css(".teamA *::text").getall())),
                "teamB": clean("".join(match.css(".teamB *::text").getall())),
                "goalsA": clean(match.css(".torA::text").get()),
                "goalsB": clean(match.css(".torB::text").get()),
                "sppStatusText": match.css(".sppStatusText::text").get(),
            }
