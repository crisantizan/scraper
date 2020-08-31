import re
import time
import sys
from core import Scraper, Browser, FileManager

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class JkAnimeSite(Scraper, FileManager):
    domain = 'https://jkanime.net/'

    def __init__(self, url, headless=True):
        Scraper.__init__(
            self,
            browser=Browser(headless=headless).browser,
            url=url,
            xpath_expressions={
                'total_episodes': '//a[@class="numbers"][last()]/text()'
            },
        )

        file_name = self.url_parts.path.split('/')[1]
        FileManager.__init__(
            self,
            folder_name=self.url_parts.netloc,
            file_name=f'{file_name}.json'
        )

    @classmethod
    def validateDomain(self, url):
        return re.match(self.domain, url) is not None

    def _format_url(self, num, url):
        # https://jkanime.net/the-god-of-high-school/9/
        path = url.path.split('/')[1]
        return f'{url.scheme}://{url.netloc}/{path}/{num}'

    def start(self):
        scope = self.get_scope()
        last = self.get_last_json_item()
        total = self.get_total_episodes(
            # get last number and clean white spaces, convert to integer
            callback=lambda res: int(res.split('-')[1].strip())
        )

        links = self.generate_links(
            total_episodes=total,
            callback=self._format_url
        )

        [links, last_episode] = self.get_new_links(
            links=links,
            last_episode=last,
            **scope
        )

        # up to date, stop program
        if not links:
            print('\n**** **** You\'re up to date with this anime! **** **** \n')
            self.browser.quit()
            sys.exit(0)

        for index, link in enumerate(links, start=last_episode):
            [iframe] = self.fetch(
                url=link,
                xpath_expression='//iframe[@class="player_conte"]/@src',
            )

            [source] = self.fetch(
                url=iframe,
                xpath_expression='//source/@src',
            )

            self.write_in_json(episode=index+1, link=source)
            print(f'Episode {index+1} done')

        self.browser.quit()
