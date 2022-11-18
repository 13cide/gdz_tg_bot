from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

from selenium.common.exceptions import NoSuchElementException

from fake_useragent import UserAgent


class Parsing:
    def __init__(self):
        self.useragent = UserAgent()

        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument(f'user-agent={self.useragent.random}')

        self.driver = webdriver.Chrome(executable_path='chromedriver',
                                  chrome_options=self.chrome_options)

        # driver.set_window_size(1500, 1000)
        self.wait_start = WebDriverWait(self.driver, 7)
        self.wait_start_long = WebDriverWait(self.driver, 30)
        self.action = ActionChains(self.driver)
    def start_parsing(self):
        self.driver.get(url='http://www.ymk.ru/')



if __name__ == '__main__':
    parsing = Parsing()
    parsing.start_parsing()