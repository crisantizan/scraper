from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self, headless=True):
        self._headless = headless

    @property
    def browser(self):
        option = webdriver.ChromeOptions()

        if self._headless:
            option.add_argument('headless')

        return webdriver.Chrome(
            ChromeDriverManager().install(),
            options=option
        )
