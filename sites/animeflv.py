import re
from core import Scraper, Browser


class AnimeFlvSite(Scraper):
    domain = 'https://www3.animeflv.net/'

    def __init__(self, url, headless=True):
        super().__init__(
            browser=Browser(headless=headless).browser,
            url=url,
            xpath_expressions={
                'total_episodes': '//ul[@id="episodeList"]/li[@class="fa-play-circle"][1]/a/p/text()'
            },
        )

    @classmethod
    def validateDomain(self, url):
        return re.match(self.domain, url) is not None

    def _format_url(self, num, url):
        # https://www3.animeflv.net/ver/boruto-naruto-next-generations-tv-161
        path = url.path.replace('/anime', '')
        return f'{url.scheme}://{url.netloc}/ver{path}-{num}'

    def start(self):
        total = self.get_total_episodes(lambda res: int(res.split(' ')[1]))
        links = self.generate_links(
            total_episodes=total,
            callback=self._format_url
        )
        print(f'TOTAL: {total}')
        print(links)

        self.browser.quit()
