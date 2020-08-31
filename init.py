import sys

from sites import AnimeFlvSite

if __name__ == '__main__':
    # available scrapers
    scrapers = [AnimeFlvSite]

    url = sys.argv[1]

    for Scraper in scrapers:
        if Scraper.validateDomain(url):
            scraper = Scraper(url=url, headless=False)
            scraper.start()

        else:
            print('Nope')
