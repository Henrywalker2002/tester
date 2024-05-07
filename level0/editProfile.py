from auto_tool.command import CommandChoices
from base import BaseTestCase
from selenium.webdriver.common.by import By


class TestEditProfile(BaseTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.login_with_account(username = 'student', password = 'moodle')

    def test_edit_success(self):
        self.command.execute(CommandChoices.CLICK, target="xpath=//a[@id='user-menu-toggle']")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/user/profile.php")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/user/edit.php?id=56&returnto=profile")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.EDIT_CONTENT, target="xpath=//input[@name='city']", value="TP.HCM")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.SELECT_OPTION, target="xpath=//select[@id='id_country']", value="value=VN")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.CLICK, target = "xpath=//input[@name='submitbutton']")
        self.command.execute(CommandChoices.PAUSE, amount=2)

    def test_edit_missing_field(self):
        self.command.execute(CommandChoices.CLICK, target="xpath=//a[@id='user-menu-toggle']")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/user/profile.php")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/user/edit.php?id=56&returnto=profile")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.EDIT_CONTENT, target="xpath=//input[@name='firstname']", value="")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.CLICK, target = "xpath=//input[@name='submitbutton']")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        assert self.driver.find_element(By.ID, "id_error_firstname").text == "- Missing given name"
        self.command.execute(CommandChoices.PAUSE, amount = 2)
    
    def test_edit_cancel(self):
        self.command.execute(CommandChoices.CLICK, target="xpath=//a[@id='user-menu-toggle']")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/user/profile.php")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/user/edit.php?id=56&returnto=profile")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.CLICK, target = "xpath=//input[@name='cancel']")
        self.command.execute(CommandChoices.PAUSE, amount=2)
    