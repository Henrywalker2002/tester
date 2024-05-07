import openpyxl
from auto_tool.command import CommandChoices
from base import BaseTestCase
from selenium.webdriver.common.by import By


class TestSendMessage(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def read_test_data(self, file_path):
        test_data = []
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data = {
                'sender': row[0],
                'recipient': row[1],
                'message': row[2]
            }
            test_data.append(data)
        return test_data

    def test_send_message(self):
        test_data = self.read_test_data('send_message_test_data.xlsx')
        for data in test_data:
            self.send_message(data)

    def send_message(self, data):
        self.command.execute(CommandChoices.OPEN, target=self.login_url)
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.INPUT, value={"username": data['sender'], "password": "moodle"})
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//button[@type='submit']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//div[@data-region='popover-region-messages']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.TYPE, target="xpath=//input[@data-region='view-overview-search-input']", value=data['recipient'])
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//button[@class='btn btn-submit icon-no-margin']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//a[@data-region='contact']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//textarea[@data-region='send-message-txt']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.TYPE, target="xpath=//textarea[@data-region='send-message-txt']", value=data['message'])
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//button[@data-action='send-message']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
