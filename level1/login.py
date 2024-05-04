from base import BaseTestCase
from auto_tool.command import CommandChoices
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import copy

class TestLogin(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.data = cls.load_data_xlsx("login")

    def test_login(self):
        for row in self.data:
            username = row.get('username', None)
            password = row.get('password', None)
            expect = row.get('expect', None)
            self.command.execute(CommandChoices.OPEN, target = self.login_url)
            self.command.execute(CommandChoices.INPUT, value = {
                "username" : username,
                "password" : password
            })
            self.command.execute(CommandChoices.CLICK, target = "xpath=//button[@type='submit']")
            if expect == "display_homepage":
                assert self.driver.current_url == self.redirect_url
                try: 
                    self.driver.find_element(By.CLASS_NAME, "navbar-brand").is_displayed()
                    assert True
                except NoSuchElementException:
                    assert False
                self.driver.delete_all_cookies()
            elif expect == "display_login_form":
                assert self.driver.find_element(By.ID, "loginerrormessage").text == "Invalid login, please try again"
                try: 
                    self.driver.find_element(By.CLASS_NAME, "navbar-brand").is_displayed()
                    assert False
                except NoSuchElementException:
                    assert True