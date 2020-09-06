# import sys

from sites import AnimeFlvSite, JkAnimeSite
from scripts import Helper

if __name__ == '__main__':
    # available scrapers
    scrapers = [AnimeFlvSite, JkAnimeSite]

    url = Helper.get_url()

    for Scraper in scrapers:
        if Scraper.validateDomain(url):
            scraper = Scraper(url=url, headless=False)
            scraper.start()
            break
        else:
            print('Nope')
