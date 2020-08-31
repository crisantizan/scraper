import re
import time
from core import Scraper, Browser, FileManager

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class AnimeFlvSite(Scraper, FileManager):
    domain = 'https://www3.animeflv.net/'

    def __init__(self, url, headless=True):
        Scraper.__init__(
            self,
            browser=Browser(headless=headless).browser,
            url=url,
            xpath_expressions={
                'total_episodes': '//ul[@id="episodeList"]/li[@class="fa-play-circle"][1]/a/p/text()'
            },
        )

        FileManager.__init__(
            self,
            folder_name=self.url_parts.netloc,
            file_name=f'{self.url_parts.path.replace("/anime/", "")}.json'
        )

    @classmethod
    def validateDomain(self, url):
        return re.match(self.domain, url) is not None

    def _format_url(self, num, url):
        # https://www3.animeflv.net/ver/boruto-naruto-next-generations-tv-161
        path = url.path.replace('/anime', '')
        return f'{url.scheme}://{url.netloc}/ver{path}-{num}'

    def start(self):
        scope = self.get_scope()
        # last = self.get_last_json_item()
        # total = self.get_total_episodes(lambda res: int(res.split(' ')[1]))
        # links = self.generate_links(
        #     total_episodes=total,
        #     callback=self._format_url
        # )
        print(scope)

        # for index, link in enumerate(links):
        #     d = self.fetch(
        #         url=link,
        #         xpath_expression='//video/@src',
        #         extends={
        #             'frame': '//div[@class="Wrapper"]//div[@id="video_box"]/iframe[1]',
        #             'click_method': EC.element_to_be_clickable((By.ID, "start"))
        #         }
        #     )

        #     self.write_in_json(episode=index+1, link=d[0])
        #     print(f'Episode {index+1} done')

        self.browser.quit()
