import re
from core import Scraper, Browser


class AnimeFlvSite(Scraper):
    domain = 'https://www3.animeflv.net/'

    def __init__(self, main_url):
        self.main_url = main_url
        self.driver = Browser().driver

        super().__init__(browser=self.driver, main_url=main_url)

    @classmethod
    def validateDomain(self, url):
        return re.match(self.domain, url) is not None
