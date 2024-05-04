from base import BaseTestCase
from auto_tool.command import CommandChoices
from selenium.webdriver.common.by import By

class TestTextSubmission(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.login_with_account(username= 'student', password='moodle')
    
    def remove_submission(self):
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/mod/assign/view.php?id=1161&action=view")
        self.command.execute(CommandChoices.CLICK, target="xpath=/html/body/div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div[2]/div/form/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div/div/div[3]/div/div[2]/form/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)

    # def test_submit_minimal(self):
    #     self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/mod/assign/view.php?id=1161&action=view")
    #     self.command.execute(CommandChoices.CLICK, target = "xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div/div/form/button")
    #     self.command.execute(CommandChoices.PAUSE, amount = 10)
    #     self.command.execute(CommandChoices.FRAME, target = "id_onlinetext_editor_ifr")
    #     self.command.execute(CommandChoices.CLICK, target= "css=html")
    #     self.command.execute(CommandChoices.TYPE, target = "id=tinymce", value = "a" * 1)
    #     self.driver.switch_to.default_content()
    #     self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
    #     self.command.execute(CommandChoices.PAUSE, amount = 5)
    #     assert self.driver.find_element(By.XPATH, "//div[2]/div[4]/div/div[2]/div/section/div[1]/div[1]/div[1]/div/div/strong").text == "Done:"
    #     self.remove_submission()

    # def test_submit_maximal(self):
    #     self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/mod/assign/view.php?id=1161&action=view")
    #     self.command.execute(CommandChoices.CLICK, target = "xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div/div/form/button")
    #     self.command.execute(CommandChoices.PAUSE, amount = 10)
    #     self.command.execute(CommandChoices.FRAME, target = "id_onlinetext_editor_ifr")
    #     self.command.execute(CommandChoices.CLICK, target= "css=html")
    #     self.command.execute(CommandChoices.TYPE, target = "id=tinymce", value = "word " * 550)
    #     self.driver.switch_to.default_content()
    #     self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
    #     self.command.execute(CommandChoices.PAUSE, amount = 5)
    #     assert self.driver.find_element(By.XPATH, "//div[2]/div[4]/div/div[2]/div/section/div[1]/div[1]/div[1]/div/div/strong").text == "Done:"

    # def test_submit_empty(self):
    #     self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/mod/assign/view.php?id=1161&action=view")
    #     self.command.execute(CommandChoices.CLICK, target = "xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div/div/form/button")
    #     self.command.execute(CommandChoices.PAUSE, amount = 6)
    #     self.command.execute(CommandChoices.FRAME, target = "id_onlinetext_editor_ifr")
    #     self.command.execute(CommandChoices.CLICK, target= "css=html")
    #     self.driver.switch_to.default_content()
    #     self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
    #     self.command.execute(CommandChoices.PAUSE, amount = 2)
    #     assert self.driver.find_element(By.XPATH, "//div[3]/div[4]/div/div[2]/div/section/div[2]/div[1]").text.split('\n')[0] == "Nothing was submitted"

    # def test_submit_greater_than_limit(self):
    #     self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/mod/assign/view.php?id=1161&action=view")
    #     self.command.execute(CommandChoices.CLICK, target = "xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div/div/form/button")
    #     self.command.execute(CommandChoices.PAUSE, amount = 6)
    #     self.command.execute(CommandChoices.FRAME, target = "id_onlinetext_editor_ifr")
    #     self.command.execute(CommandChoices.CLICK, target= "css=html")
    #     self.command.execute(CommandChoices.TYPE, target = "id=tinymce", value = "word " * 551)
    #     self.driver.switch_to.default_content()
    #     self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
    #     self.command.execute(CommandChoices.PAUSE, amount = 2)
    #     assert self.driver.find_element(By.XPATH, "//div[3]/div[4]/div/div[2]/div/section/div[2]/div[1]/span").text == "The word limit for this assignment is 550 words and you are attempting to submit 551 words. Please review your submission and try again."

    # def test_submit_great_than_minimal(self):
    #     self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/mod/assign/view.php?id=1161&action=view")
    #     self.command.execute(CommandChoices.CLICK, target = "xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div/div/form/button")
    #     self.command.execute(CommandChoices.PAUSE, amount = 10)
    #     self.command.execute(CommandChoices.FRAME, target = "id_onlinetext_editor_ifr")
    #     self.command.execute(CommandChoices.CLICK, target= "css=html")
    #     self.command.execute(CommandChoices.TYPE, target = "id=tinymce", value = "word " * 2)
    #     self.driver.switch_to.default_content()
    #     self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
    #     self.command.execute(CommandChoices.PAUSE, amount = 5)
    #     assert self.driver.find_element(By.XPATH, "//div[2]/div[4]/div/div[2]/div/section/div[1]/div[1]/div[1]/div/div/strong").text == "Done:"
    #     self.remove_submission()

    def test_submit_less_than_maximal(self):
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/mod/assign/view.php?id=1161&action=view")
        self.command.execute(CommandChoices.CLICK, target = "xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div/div/form/button")
        self.command.execute(CommandChoices.PAUSE, amount = 10)
        self.command.execute(CommandChoices.FRAME, target = "id_onlinetext_editor_ifr")
        self.command.execute(CommandChoices.CLICK, target= "css=html")
        self.command.execute(CommandChoices.TYPE, target = "id=tinymce", value = "word " * 549)
        self.driver.switch_to.default_content()
        self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        assert self.driver.find_element(By.XPATH, "//div[2]/div[4]/div/div[2]/div/section/div[1]/div[1]/div[1]/div/div/strong").text == "Done:"
        assert self.driver.find_element(By.XPATH, "//td[contains(.,'Submitted for grading')]").is_displayed()
        self.remove_submission()