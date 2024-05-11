import copy

import openpyxl
from base import BaseTestCase
from selenium.webdriver.common.by import By

from auto_tool.command import CommandChoices


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
                'firstname': "" if row[0] is None else row[0],
                'lastname': "" if row[1] is None else row[1],
                'city': row[2],
                'country': 'value='+row[3],
                'action': row[4],
                'expect': row[5],
                'error': row[6]
            }
            test_data.append(data)
        return test_data

    def check_error(self, field, value):
        if field == 'firstname':
            assert self.driver.find_element(By.ID, 'id_error_firstname').text == value
        elif field == 'lastname':
            assert self.driver.find_element(By.ID, 'id_error_lastname').text == value
        else:
            assert False

    def edit_profile(self, data):
        self.command.execute(CommandChoices.CLICK, target="xpath=//a[@id='user-menu-toggle']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/user/profile.php")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/user/edit.php?id=56&returnto=profile")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.EDIT_CONTENT, target="xpath=//input[@name='firstname']", value=data['firstname'])
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.EDIT_CONTENT, target="xpath=//input[@name='lastname']", value=data['lastname'])
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.EDIT_CONTENT, target="xpath=//input[@name='city']", value=data['city'])
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.SELECT_OPTION, target="xpath=//select[@id='id_country']", value= data['country'])
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@name='submitbutton']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        if data['error'] != 'none':
            field, text_error = data['error'].split(':')
            self.check_error(field, text_error)


    def edit_cancel(self,data):
        self.command.execute(CommandChoices.CLICK, target="xpath=//a[@id='user-menu-toggle']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/user/profile.php")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/user/edit.php?id=56&returnto=profile")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.EDIT_CONTENT, target="xpath=//input[@name='firstname']", value=data['firstname'])
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.EDIT_CONTENT, target="xpath=//input[@name='lastname']", value=data['lastname'])
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.EDIT_CONTENT, target="xpath=//input[@name='city']", value=data['city'])
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.SELECT_OPTION, target="xpath=//select[@id='id_country']", value=data['country'])
        self.command.execute(CommandChoices.PAUSE, amount=5)
        if data['error'] != 'none':
            field, text_error = data['error'].split(':')
            self.check_error(field, text_error)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@name='cancel']")
        self.command.execute(CommandChoices.PAUSE, amount=5)


    def test(self):
        test_data = self.read_test_data('edit_profile_test_data.xlsx')
        for data in test_data:
            if data['action'] == 'edit':
                self.edit_profile(data)
            else:
                self.edit_cancel(data)
    