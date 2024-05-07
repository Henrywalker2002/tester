import openpyxl
from auto_tool.command import CommandChoices
from base import BaseTestCase
from selenium.webdriver.common.by import By


class TestEditProfile(BaseTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.login_with_account(username='student', password='moodle')

    def read_test_data(self, file_path):
        test_data = []
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data = {
                'city': row[0],
                'country': row[1],
                'error_firstname': row[2],
                'cancel': row[3]
            }
            test_data.append(data)
        return test_data

    def test_edit_profile_with_data(self):
        test_data = self.read_test_data('edit_profile_test_data.xlsx')
        for data in test_data:
            self.edit_profile(data)

    def edit_profile(self, data):
        self.command.execute(CommandChoices.CLICK, target="xpath=//a[@id='user-menu-toggle']")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/user/profile.php")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/user/edit.php?id=56&returnto=profile")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.EDIT_CONTENT, target="xpath=//input[@name='city']", value=data['city'])
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.SELECT_OPTION, target="xpath=//select[@id='id_country']", value=data['country'])
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@name='submitbutton']")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        if 'error_firstname' in data:
            error_message = self.driver.find_element(By.ID, "id_error_firstname").text
            assert error_message == data['error_firstname']
            self.command.execute(CommandChoices.PAUSE, amount=2)
        elif 'cancel' in data and data['cancel'].lower() == 'true':
            self.command.execute(CommandChoices.CLICK, target="xpath=//input[@name='cancel']")
            self.command.execute(CommandChoices.PAUSE, amount=2)
