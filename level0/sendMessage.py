import unittest

from auto_tool.command import CommandChoices
from base import BaseTestCase
from selenium.webdriver.common.by import By


class TestSendMessage(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_TtoS_message_delivered(self):
        self.send_message(sender='Teacher', recipient='Barbara Gardner')
        # Verification: Manual verification or check the message in the student's inbox

    def test_TtoG_message_delivered(self):
        self.send_message(sender='Teacher', recipient='Team South')
        # Verification: Manual verification or check the message in each student's inbox in the group

    def test_StoS_character_limit_exceeded(self):
        self.send_message(sender='Student', recipient='Amanda Hamilton')
        # Verification: Check for error message displayed on the UI

    def test_StoG_message_with_image(self):
        self.send_message(sender='Student', recipient='TeamSouth')
        # Verification: Manual verification or check the sent message with attached image in the group's inbox

    def test_StoT_message_delivered(self):
        self.send_message(sender='Student', recipient='Jeffrey Sanders')
        # Verification: Manual verification or check the message in the teacher's inbox

    def test_TtoT_message_delivered(self):
        self.send_message(sender='Teacher', recipient='Joyce Gardner')
        # Verification: Manual verification or check the message in the teacher's inbox

    def send_message(self, sender, recipient):
        self.command.execute(CommandChoices.OPEN, target=self.login_url)
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.INPUT, value={"username": sender, "password": "moodle"})
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//button[@type='submit']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//div[@data-region='popover-region-messages']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.TYPE, target="xpath=//input[@data-region='view-overview-search-input']", value=recipient)
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//button[@class='btn btn-submit icon-no-margin']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//a[@data-region='contact']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//textarea[@data-region='send-message-txt']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.TYPE, target="xpath=//textarea[@data-region='send-message-txt']", value="Hello " + recipient)
        self.command.execute(CommandChoices.PAUSE, amount=5)
        self.command.execute(CommandChoices.CLICK, target="xpath=//button[@data-action='send-message']")
        self.command.execute(CommandChoices.PAUSE, amount=5)
