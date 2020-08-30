import sys

from sites import AnimeFlvSite

if __name__ == '__main__':
    # available scrapers
    scrapers = [AnimeFlvSite]

    url = sys.argv[1]

    for scraper in scrapers:
        if scraper.validateDomain(url):
            print('Yepe')
        else:
            print('Nope')
