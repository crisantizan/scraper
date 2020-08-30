import time
from lxml import html
import os
from helper import get_domain


class Scraper:
    def __init__(self, browser, main_url):
        self.browser = browser
        self.main_url = main_url
        self.domain = get_domain(url=main_url)

    def fetch(self, url, xpath_expression):
        self.browser.get(url)

        while True:
            time.sleep(0.5)
            data = self._scrape(xpath_expression)
            if data:
                return data

    def _scrape(self, xpath_expression):
        # get the innerhtml from the rendered page
        innerHTML = self.browser.execute_script(
            "return document.body.innerHTML")
        # Now use lxml to parse the page
        parsed = html.fromstring(innerHTML)
        # Get your element with xpath
        return parsed.xpath(xpath_expression)
