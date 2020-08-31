import time
import os
import sys

from lxml import html

from helper import get_domain


class Scraper:
    def __init__(self, browser, url, xpath_expressions):
        self.browser = browser
        self.url = url
        self.domain = get_domain(url=url)
        self.xpath = xpath_expressions

        self._validate_xpath_dict()

    def fetch(self, url, xpath_expression):
        self.browser.get(url)

        while True:
            time.sleep(0.5)
            data = self._scrape(xpath_expression)
            if data:
                return data

    def get_total_episodes(self, callback):
        [response] = self.fetch(
            url=self.url,
            xpath_expression=self.xpath['total_episodes']
        )

        return callback(response)

    def _scrape(self, xpath_expression):
        # get the innerhtml from the rendered page
        innerHTML = self.browser.execute_script(
            "return document.body.innerHTML")
        # Now use lxml to parse the page
        parsed = html.fromstring(innerHTML)
        # Get your element with xpath
        return parsed.xpath(xpath_expression)

    def _validate_xpath_dict(self):
        keys = ['total_episodes']

        for key in keys:
            if not key in self.xpath:
                print(f'Xpath expression "{key}" is required!')
                sys.exit(1)