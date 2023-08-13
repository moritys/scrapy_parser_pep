import scrapy

from pep_parse.items import PepParseItem
from pep_parse.constants import MAIN_PEP_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = [MAIN_PEP_URL]

    def parse(self, response):
        all_peps = response.css('a.pep::attr(href)').getall()
        for pep_link in all_peps:
            yield response.follow(f'{pep_link}/', callback=self.parse_pep)

    def parse_pep(self, response):
        header = response.css('h1.page-title::text').get()
        number = header.split(' – ')[0].split()[-1]
        name = header.split(' – ')[-1]
        status = response.css('dt:contains("Status") + dd > abbr::text').get()

        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
