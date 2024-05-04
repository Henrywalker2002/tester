from base import BaseTestCase
from auto_tool.command import CommandChoices
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import copy
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "submit_file")
class TestFileSubmission(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.assignment_url = "https://school.moodledemo.net/mod/assign/view.php?id=1210&forceview=1"
        # cls.prepare_enviroment(cls)
        cls.login_with_account(username= 'student', password='moodle')
        cls.data = cls.load_data_xlsx("fileSubmission")

    def prepare_enviroment(self):
        self.login_with_account(username= 'teacher', password='moodle')
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/course/modedit.php?add=assign&type&course=51&section=4&return=0&beforemod=0")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.TYPE, target = "id=id_name", value = "Test File Submission")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.SELECT_OPTION, target = "id=id_assignsubmission_file_maxfiles", value = "value=1")
        self.command.execute(CommandChoices.TYPE, target="id=id_assignsubmission_file_filetypes", value="pdf,doc,docx")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
        self.command.execute(CommandChoices.PAUSE, amount = 10)
        self.assignment_url = self.driver.current_url
        self.command.execute(CommandChoices.CLICK, target = "xpath=//div[2]/nav/div/div[2]/div[5]")
        self.command.execute(CommandChoices.CLICK, target = "xpath=//div[2]/nav/div/div[2]/div[5]/div/div/div/div/div/div[1]/a[10]")        
        self.driver.delete_all_cookies()

    def go_to_submit_file(self):
        self.command.execute(CommandChoices.OPEN, target = self.assignment_url)
        self.command.execute(CommandChoices.CLICK, target="xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div/div/form/button")
        self.command.execute(CommandChoices.PAUSE, amount = 5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div/form/fieldset/div[2]/div/div[2]/fieldset/div[1]/div[2]/div[1]/div[1]/div[1]/a")
        self.command.execute(CommandChoices.PAUSE, amount = 3)
    
    def remove_submission(self):
        self.command.execute(CommandChoices.OPEN, target = self.assignment_url)
        self.command.execute(CommandChoices.CLICK, target="xpath=/html/body/div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div[2]/div/form/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div/div/div[3]/div/div[2]/form/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)

    def test_file_submission(self):
        for row in self.data:
            file_name = row.get('file_name', None)
            expect = row.get('expect', None)
            element = row.get('element', None)
            error_msg = row.get('error_msg', None)
            self.go_to_submit_file()
            upload_file = os.path.join(FILE_PATH, file_name)

            self.command.execute(CommandChoices.CLICK, target = "xpath=//span[contains(.,'Upload a file')]")
            self.command.execute(CommandChoices.TYPE, target="css=input[type='file']", value=upload_file)
            self.command.execute(CommandChoices.CLICK, target = "xpath=//div[7]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/button")
            self.command.execute(CommandChoices.PAUSE, amount = 2)
            
            if expect == "display_success":
                self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
                self.command.execute(CommandChoices.PAUSE, amount = 2)
                try: 
                    self.driver.find_element(By.XPATH, element).is_displayed()
                    assert True
                except NoSuchElementException:
                    assert False
                self.remove_submission()
            elif expect == "display_error":
                try:
                    assert self.driver.find_element(By.XPATH, element).is_displayed()
                    assert self.driver.find_element(By.XPATH, element).text == error_msg
                except NoSuchElementException:
                    assert False