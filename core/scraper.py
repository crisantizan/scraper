import time
import os
import sys

from lxml import html
from selenium.webdriver.support.ui import WebDriverWait

import helper


class Scraper():
    def __init__(self, browser, url, xpath_expressions):
        self.url_parts = helper.split_url(url=url)
        self.browser = browser
        self.url = url
        self.xpath = xpath_expressions

        self._validate_xpath_dict()

    def fetch(self, url, xpath_expression, extends=None):
        self.browser.get(url)

        if extends:
            if 'frame' in extends:
                while True:
                    try:
                        self.browser.switch_to_frame(
                            self.browser.find_element_by_xpath(
                                extends['frame']
                            )
                        )
                        break
                    except:
                        print('Opps! retrying...')

            if 'click_method' in extends:
                element = WebDriverWait(self.browser, 20).until(
                    extends['click_method']
                )
                element.click()

        while True:
            time.sleep(0.5)
            data = self.scrape(xpath_expression)
            if data:
                return data

    def get_total_episodes(self, callback):
        [response] = self.fetch(
            url=self.url,
            xpath_expression=self.xpath['total_episodes']
        )

        return callback(response)

    def generate_links(self, total_episodes, callback):
        links = []
        for episode in range(1, total_episodes + 1):
            links.append(callback(episode, self.url_parts))

        return links

    def get_scope(self):
        scope = None

        # default values
        start = 0
        end = -1

        # if the custom scope already passed
        try:
            scope = sys.argv[2]
            temp = scope.split(':')

            if len(temp) > 0:
                # verify custom scope
                for index, val in enumerate(temp):
                    if not val.isnumeric():
                        print('\nScope param should be a numeric value')
                        sys.exit(1)

                    temp[index] = int(temp[index])

                if temp[0] > 1:
                    start = temp[0] - 1

                if temp[1] and temp[1] > start:
                    end = temp[1]

            # return values
            return {'start': start, 'end': end}
        except:
            return {'start': start, 'end': end}

    def get_new_links(self, links, last_episode, start, end):
        length = len(links)
        if (start == 0 and end == -1) or not (start <= length and end <= length):
            # normal, verify last episode
            if last_episode == 0:
                return [links, 0]
            else:
                return [links[last_episode:], last_episode]

        if last_episode >= start + 1:
            if last_episode < end:
                return [links[last_episode:end], last_episode]

            return [[], start]
        elif start > 0 and end == -1:
            # from x to final
            return [links[start:], start]
        else:
            # from x to x
            return [links[start:end], start]

    def scrape(self, xpath_expression):
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
