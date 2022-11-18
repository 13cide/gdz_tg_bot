import time

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
from bs4 import BeautifulSoup


from fake_useragent import UserAgent
import time

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

    def start_parsing(self, login, password):
        try:
            self.driver.get(url='http://www.ymk.ru/')
            self.driver.implicitly_wait(2)

            login_area = self.driver.find_element(By.ID, 'login')
            login_area.click()
            login_area.clear()
            login_area.send_keys(login)

            password_area = self.driver.find_element(By.ID, 'psw')
            password_area.click()
            password_area.clear()
            password_area.send_keys(password)

            accept = self.driver.find_elements(By.CLASS_NAME, 'button')[0]
            accept.click()

            self.driver.get(url='http://www.ymk.ru/ymk/index.php?module=pupils&action=ShowDiary')
            time.sleep(2)

            soup = BeautifulSoup(self.driver.page_source, 'lxml')

            marks = soup.find_all('a', {'class': 'diary_link'})
            i = 0
            for mark in marks:
                print(mark.text)
                if mark.text.strip().isdigit():
                    try:
                        marks_links = self.driver.find_elements(By.CLASS_NAME, 'diary_link')
                        mark_link = marks_links[i]
                        mark_link.click()
                        time.sleep(2)
                        self.driver.back()
                    except:
                        pass
                i+=1
        except NoSuchElementException as ex:
            print(ex)
        finally:
            time.sleep(10000)
            self.driver.close()
            self.driver.quit()
