from base import BaseTestCase
from auto_tool.command import CommandChoices
from selenium.webdriver.common.by import By
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "submit_file")

class TestFileSubmission(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.assignment_url = ""
        cls.prepare_enviroment(cls)
        cls.login_with_account(username= 'student', password='moodle')

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
    
    def remove_submission(self):
        self.command.execute(CommandChoices.OPEN, target = self.assignment_url)
        self.command.execute(CommandChoices.CLICK, target="xpath=/html/body/div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div[2]/div/form/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div/div/div[3]/div/div[2]/form/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
    
    def go_to_submit_file(self):
        self.command.execute(CommandChoices.OPEN, target = self.assignment_url)
        self.command.execute(CommandChoices.CLICK, target="xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div[1]/div/div/div/form/button")
        self.command.execute(CommandChoices.PAUSE, amount = 5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//div[2]/div[4]/div/div[2]/div/section/div[2]/div/form/fieldset/div[2]/div/div[2]/fieldset/div[1]/div[2]/div[1]/div[1]/div[1]/a")
        self.command.execute(CommandChoices.PAUSE, amount = 3)
        self.command.execute(CommandChoices.CLICK, target = "xpath=//span[contains(.,'Upload a file')]")
    
    def test_file_submission_wrong_size_file_1(self):
        self.go_to_submit_file()
        self.command.execute(CommandChoices.TYPE, target="css=input[type='file']", value= os.path.join(FILE_PATH, "1MB.pdf"))
        self.command.execute(CommandChoices.CLICK, target = "xpath=//div[7]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        assert self.driver.find_element(By.XPATH, "//div[9]/div[3]/div/div[1]/h5").text == "Error"
        assert self.driver.find_element(By.XPATH, "//div[9]/div[3]/div/div[2]/div/div[1]").text == "The file 1MB.pdf is too large. The maximum size you can upload is 1 MB."

    def test_file_submission_wrong_size_file_2(self):
        self.go_to_submit_file()
        self.command.execute(CommandChoices.TYPE, target="css=input[type='file']", value="C:\\Users\\thanh\\SourcefromMe\\tester\\level0\\submit_file\\1.5MB.pdf")
        self.command.execute(CommandChoices.CLICK, target = "xpath=//div[7]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        assert self.driver.find_element(By.XPATH, "//div[9]/div[3]/div/div[1]/h5").text == "Error"
        assert self.driver.find_element(By.XPATH, "//div[9]/div[3]/div/div[2]/div/div[1]").text == "The file 1.5MB.pdf is too large. The maximum size you can upload is 1 MB."

    def test_file_submission_wrong_file_type_1(self):
        self.go_to_submit_file()
        self.command.execute(CommandChoices.TYPE, target="css=input[type='file']", value="C:\\Users\\thanh\\SourcefromMe\\tester\\level0\\submit_file\\0.5MB.xlsx")
        self.command.execute(CommandChoices.CLICK, target = "xpath=//div[7]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        assert self.driver.find_element(By.XPATH, "//div[9]/div[3]/div/div[1]/h5").text == "Error"
        assert self.driver.find_element(By.XPATH, "//div[9]/div[3]/div/div[2]/div/div[1]").text == "Excel 2007 spreadsheet filetype cannot be accepted."

    def test_file_submission_wrong_file_type_2(self):
        self.go_to_submit_file()
        self.command.execute(CommandChoices.TYPE, target="css=input[type='file']", value="C:\\Users\\thanh\\SourcefromMe\\tester\\level0\\submit_file\\1MB.xlsx")
        self.command.execute(CommandChoices.CLICK, target = "xpath=//div[7]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        assert self.driver.find_element(By.XPATH, "//div[9]/div[3]/div/div[1]/h5").text == "Error"
        assert self.driver.find_element(By.XPATH, "//div[9]/div[3]/div/div[2]/div/div[1]").text == "Excel 2007 spreadsheet filetype cannot be accepted."
    
    def test_file_submission_wrong_file_type_3(self):
        self.go_to_submit_file()
        self.command.execute(CommandChoices.TYPE, target="css=input[type='file']", value="C:\\Users\\thanh\\SourcefromMe\\tester\\level0\\submit_file\\1.5MB.xlsx")
        self.command.execute(CommandChoices.CLICK, target = "xpath=//div[7]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        assert self.driver.find_element(By.XPATH, "//div[9]/div[3]/div/div[1]/h5").text == "Error"
        assert self.driver.find_element(By.XPATH, "//div[9]/div[3]/div/div[2]/div/div[1]").text == "Excel 2007 spreadsheet filetype cannot be accepted."

    def test_file_submission(self):
        self.go_to_submit_file()
        self.command.execute(CommandChoices.TYPE, target="css=input[type='file']", value="C:\\Users\\thanh\\SourcefromMe\\tester\\level0\\submit_file\\350KB.pdf")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target = "xpath=//div[7]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/button")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        assert self.driver.find_element(By.XPATH, "//div[2]/div[4]/div/div[2]/div/section/div[2]/div[2]/div/div/table/tbody/tr[1]/td").text == "Submitted for grading"