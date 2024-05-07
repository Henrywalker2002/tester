from auto_tool.command import CommandChoices
from base import BaseTestCase
from selenium.webdriver.common.by import By


class TestExportCalendar(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.login_with_account(username= 'student', password='moodle')

    def test_export_success(self):
        self.command.execute(CommandChoices.CLICK, target = "xpath=//a[@id='user-menu-toggle']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/view.php?view=month")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/managesubscriptions.php")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/export.php")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_events_exportevents_all']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_period_timeperiod_weeknow']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_export']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)

    def test_export_missing_select(self):
        self.command.execute(CommandChoices.CLICK, target = "xpath=//a[@id='user-menu-toggle']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/view.php?view=month")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/managesubscriptions.php")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/export.php")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_events_exportevents_all']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_export']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        assert self.driver.find_element(By.ID, "fgroup_id_error_period").text == "Required"
        self.command.execute(CommandChoices.PAUSE, amount = 2)
    
    def test_geturl(self):
        self.command.execute(CommandChoices.CLICK, target = "xpath=//a[@id='user-menu-toggle']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/view.php?view=month")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/managesubscriptions.php")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/export.php")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_events_exportevents_all']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_period_timeperiod_weeknow']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_generateurl']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
    
    def test_geturl_missing_select(self):
        self.command.execute(CommandChoices.CLICK, target = "xpath=//a[@id='user-menu-toggle']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/view.php?view=month")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/managesubscriptions.php")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/export.php")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_events_exportevents_all']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_generateurl']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        assert self.driver.find_element(By.ID, "fgroup_id_error_period").text == "Required"
        self.command.execute(CommandChoices.PAUSE, amount = 2)

    def test_gohome(self):
        self.command.execute(CommandChoices.CLICK, target = "xpath=//a[@id='user-menu-toggle']")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/view.php?view=month")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/managesubscriptions.php")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target = "https://school.moodledemo.net/calendar/export.php")
        self.command.execute(CommandChoices.PAUSE, amount = 2)
        self.command.execute(CommandChoices.OPEN, target= "https://school.moodledemo.net/?redirect=0")
        self.command.execute(CommandChoices.PAUSE, amount = 2)