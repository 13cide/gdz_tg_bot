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

class Parsing:
    def __init__(self):
        self.useragent = UserAgent()

        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument(f'user-agent={self.useragent.random}')

        self.driver = webdriver.Chrome(executable_path='chromedriver',
                                  chrome_options=self.chrome_options)

        self.driver.set_window_size(1500, 1000)
        self.wait_start = WebDriverWait(self.driver, 7)
        self.wait_start_long = WebDriverWait(self.driver, 30)
        self.action = ActionChains(self.driver)

    def start_parsing(self, login, password, name):
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
                if mark.text.strip().isdigit():
                    try:
                        marks_links = self.driver.find_elements(By.CLASS_NAME, 'diary_link')
                        mark_link = marks_links[i]
                        mark_link.click()
                        time.sleep(1)

                        soup_tests = BeautifulSoup(self.driver.page_source, 'lxml')
                        tests = soup_tests.find_all('tr', {'class': 'content'})

                        subject = soup_tests.find('td', {'class': 'content'}).text.split('\n')[3].strip().replace('Предмет : ', '').replace(' ', '_')
                        test_title = soup_tests.find('td', {'class': 'content_title'}).text.strip().replace('№', '_').replace(' ', '')
                    except:
                        i += 1
                        pass
                    i1 = 0
                    i1_test = 1
                    for test in tests:
                        try:
                            tests_link = self.driver.find_elements(By.CLASS_NAME, 'content')[2:]
                            test_link = tests_link[i1]
                            test_link.click()

                            self.driver.find_element(By.ID, 'frmTask').screenshot(f'screenshot\\{name.replace(" ", "_")}_{subject}_{test_title}_задание_{i1_test}.png')
                            i1_test += 1

                            self.driver.back()
                        except:
                            i1 += 1

                        i1+=1
                    self.driver.back()
                i+=1

        except NoSuchElementException as ex:
            print(ex)
        finally:
            time.sleep(10000)
            self.driver.close()
            self.driver.quit()
