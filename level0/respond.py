from base import BaseTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestRespond(BaseTestCase):

    def test(self):
        driver = webdriver.Edge()
        driver.get("https://moodle.org/demo")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        response_time = driver.execute_script("return (window.performance.timing.responseEnd - window.performance.timing.navigationStart);")

        print("Respond time: {} ms".format(response_time))

        driver.quit()
