from base import BaseTestCase
from selenium.webdriver.common.by import By

from auto_tool.command import CommandChoices


class TestAddUser(BaseTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.login_with_account(username= 'manager', password='moodle')
    
    def test_add_success(self):
        input = {
            "username" : "username123",
            "firstname" : "firstname",  
            "lastname" : "lastname",
            "email" : "email@example.com"
        }
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/user/editadvanced.php?id=-1")
        self.command.execute(CommandChoices.INPUT, value = input)
        self.command.execute(CommandChoices.CLICK, target = "xpath=//a[@data-passwordunmask='edit']")
        self.command.execute(CommandChoices.TYPE, target = "xpath=//input[@name='newpassword']", value = "password")
        self.command.execute(CommandChoices.PAUSE, amount = 5)
        self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
        self.command.execute(CommandChoices.PAUSE, amount = 5)
        assert self.driver.current_url == "https://school.moodledemo.net/admin/user.php"
        self.command.execute(CommandChoices.CLICK, target = "xpath=//button[@title='Filters']")
        self.command.execute(CommandChoices.SELECT_OPTION, 
                            target = "xpath=//select[@name='user:username_operator']", 
                            value = "text=Is equal to")
        self.command.execute(CommandChoices.TYPE, target = "xpath=//input[@name='user:username_value']", value = input["username"])
        self.command.execute(CommandChoices.CLICK, target = "xpath=//input[@value='Apply']")
        self.driver.find_element(By.XPATH, f"xpath=//td[text()='{input['email']}']")
    
    def test_fail_missing_username(self):
        input = {
            "firstname" : "firstname",  
            "lastname" : "lastname",
            "email" : "email@email.com",
        }
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/user/editadvanced.php?id=-1")
        self.command.execute(CommandChoices.INPUT, value = input)
        self.command.execute(CommandChoices.CLICK, target = "xpath=//a[@data-passwordunmask='edit']")
        self.command.execute(CommandChoices.TYPE, target = "xpath=//input[@name='newpassword']", value = "password")
        self.command.execute(CommandChoices.PAUSE, amount = 5)
        self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
        self.command.execute(CommandChoices.PAUSE, amount = 5)
        assert self.driver.current_url != "https://school.moodledemo.net/admin/user.php"
        assert self.driver.find_element(By.ID, "id_error_username").text == "Required"