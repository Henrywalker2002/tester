from base import BaseTestCase
from command import CommandChoices
from selenium.webdriver.common.by import By
import copy


class TestAddUser(BaseTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.data = cls.load_data_xlsx("addUser")
        cls.login_with_account(username= 'manager', password='moodle')
    
    def input_data(self, data: dict):
        data = copy.deepcopy(data)
        data.pop('expect', None)
        data.pop('error field', None)
        data.pop('stt', None)
        password = data.pop('password', None)
        input = data
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/user/editadvanced.php?id=-1")
        self.command.execute(CommandChoices.INPUT, value = input)
        self.command.execute(CommandChoices.CLICK, target = "xpath=//a[@data-passwordunmask='edit']")
        self.command.execute(CommandChoices.TYPE, target = "xpath=//input[@name='newpassword']", value = password)
        self.command.execute(CommandChoices.PAUSE, amount = 5)
        self.command.execute(CommandChoices.CLICK, target = "id=id_submitbutton")
        self.command.execute(CommandChoices.PAUSE, amount = 5)
    
    def check_error(self, field, value):
        if field == "username":
            assert self.driver.find_element(By.ID, "id_error_username").text == value
        elif field == "email":
            assert self.driver.find_element(By.ID, "id_error_email").text == value
        else :
            assert False
    
    def test(self):
        for row in self.data:
            self.input_data(row)
            expect = row.get('expect', None)
            if expect == "success":
                assert self.driver.current_url == expect
            else:
                field, text_error = row['error field'].split(':')
                self.check_error(field, text_error)
        