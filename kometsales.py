from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

BASE_URL = "https://app.kometsales.com"

TIMEOUT = 30

class SignIn(object):
    """docstring for SignCheck"""

    def __init__(self, browser, username, password, url=BASE_URL, *args, **kwargs):

        self.username = username
        self.password = password
        self.url = url
        self.browser = browser

    def sign_in(self):
        try:
            self.browser.get(self.url)

            # Waits until form div is loaded
            element = WebDriverWait(self.browser, TIMEOUT).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "form"))
            )

            time.sleep(1)  # Gives an additional seconds
            user_box = self.browser.find_element_by_id("txtUserName")
            pass_box = self.browser.find_element_by_id("txtPassword")

            user_box.send_keys(self.username)
            pass_box.send_keys(self.password)

            # makes clic on login button
            self.browser.find_element_by_xpath(
                '//button[text()="Ingresar"]').click()
            return True

        except Exception as e:
            print("[ERROR] Could not make login,")
            print("details below \n {}".format(e))
            return False


def test(browser, username, password):
    sign_in = SignIn(browser, username, password)
    result = sign_in.sign_in()

    if not result:
        return False
    
    time.sleep(10)

    if 'Komet Sales'.lower() not in browser.title.lower():  # The user is in his account
        return True
    
    return False

def main():
    browser = webdriver.Chrome()

    print("[INFO] Running test with parameters: [Username:gp], [Pass:demo]")
    result = test(browser, "gp", "demo")
    print("[INFO] Test result:{}".format(result))
    browser.quit()

    browser = webdriver.Chrome()
    print("[INFO] Running test with parameters: [Username:gp1], [Pass:demo]")
    result = test(browser, "gp1", "demo")
    print("[INFO] Test result:{}".format(result))

    browser.quit()

main()
