from base import BaseTestCase
from auto_tool.command import CommandChoices
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import copy

class TestTextSubmission(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.data = cls.load_data_xlsx("textSubmission")
        cls.login_with_account(username= 'student', password='moodle')

    def remove_submission(self):
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/mod/assign/view.php?id=1161&action=view")
        self.command.execute(CommandChoices.CLICK, target="xpath=/html/body/div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div[2]/div/form/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div/div/div[3]/div/div[2]/form/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        
    def test_text_submission(self):
        for row in self.data:
            num_of_words = row.get('num_of_word', None)
            expect = row.get('expect', None)
            element = row.get('element', None)
            msg = row.get('error_msg', None)
            self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/mod/assign/view.php?id=1161&action=view")
            self.command.execute(CommandChoices.CLICK, target = "xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div/div/form/button")
            self.command.execute(CommandChoices.PAUSE, amount = 6)
            self.command.execute(CommandChoices.FRAME, target = "id_onlinetext_editor_ifr")
            self.command.execute(CommandChoices.CLICK, target= "css=html")
            if num_of_words > 0: 
                self.command.execute(CommandChoices.TYPE, target = "id=tinymce", value = "word " * num_of_words)
            self.driver.switch_to.default_content()
            self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
            if expect == "display_result":
                try: 
                    self.driver.find_element(By.XPATH, element).is_displayed()
                    assert True
                except NoSuchElementException:
                    assert False
                self.remove_submission()
            elif expect == "display_limit_error":
                try:
                    assert self.driver.find_element(By.XPATH, element).is_displayed()
                    assert self.driver.find_element(By.XPATH, element).text == msg
                except NoSuchElementException:
                    assert False
            elif expect == "display_nothing":
                try:
                    assert self.driver.find_element(By.XPATH, element).text.split('\n')[0] == msg
                except NoSuchElementException:
                    assert False