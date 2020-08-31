import sys

from sites import AnimeFlvSite, JkAnimeSite

from helper import get_url

if __name__ == '__main__':
    # available scrapers
    scrapers = [AnimeFlvSite, JkAnimeSite]

    url = get_url()

    for Scraper in scrapers:
        if Scraper.validateDomain(url):
            scraper = Scraper(url=url, headless=False)
            scraper.start()

        else:
            print('Nope')
