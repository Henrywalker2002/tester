from base import BaseTestCase
from auto_tool.command import CommandChoices
from selenium.webdriver.common.by import By

class TestLogin(BaseTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
    def test_login_wrong_password(self):
        self.command.execute(CommandChoices.OPEN, target = self.login_url)
        self.command.execute(CommandChoices.INPUT, value = {
            "username" : "student",
            "password" : "wrongpassword"
        })
        self.command.execute(CommandChoices.CLICK, target = "xpath=//button[@type='submit']")
        assert self.driver.current_url != self.redirect_url
        assert self.driver.find_element(By.ID, "loginerrormessage").text == "Invalid login, please try again"

    def test_login_wrong_username(self):
        self.command.execute(CommandChoices.OPEN, target = self.login_url)
        self.command.execute(CommandChoices.INPUT, value = {
            "username" : "wrongusername",
            "password" : "moodle"
        })
        self.command.execute(CommandChoices.CLICK, target = "xpath=//button[@type='submit']")
        assert self.driver.current_url != self.redirect_url
        assert self.driver.find_element(By.ID, "loginerrormessage").text == "Invalid login, please try again"

    def test_login_wrong_password_and_username(self):
        self.command.execute(CommandChoices.OPEN, target = self.login_url)
        self.command.execute(CommandChoices.INPUT, value = {
            "username" : "wrongusername",
            "password" : "wrongpassword"
        })
        self.command.execute(CommandChoices.CLICK, target = "xpath=//button[@type='submit']")
        assert self.driver.current_url != self.redirect_url
        assert self.driver.find_element(By.ID, "loginerrormessage").text == "Invalid login, please try again"

    def test_login_success(self):
        self.command.execute(CommandChoices.OPEN, target = self.login_url)
        self.command.execute(CommandChoices.INPUT, value = {
            "username" : "student",
            "password" : "moodle"
        })
        self.command.execute(CommandChoices.CLICK, target = "xpath=//button[@type='submit']")
        assert self.driver.current_url == self.redirect_url
        assert self.driver.find_element(By.CLASS_NAME, "navbar-brand").is_displayed()
        self.command.execute(CommandChoices.CLICK, target = "xpath=//div[2]/nav/div/div[2]/div[5]")
        self.command.execute(CommandChoices.CLICK, target = "xpath=//div[2]/nav/div/div[2]/div[5]/div/div/div/div/div/div[1]/a[9]")        
        self.driver.delete_all_cookies()

