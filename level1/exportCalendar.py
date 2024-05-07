import openpyxl
from auto_tool.command import CommandChoices
from base import BaseTestCase
from selenium.webdriver.common.by import By


class TestExportCalendar(BaseTestCase):

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
                'export_events_all': row[0],
                'period_timeperiod_weeknow': row[1],
                'click_export': row[2],
                'generate_url': row[3],
                'assert_error_message': row[4],
                'open_home': row[5]
            }
            test_data.append(data)
        return test_data

    def test_export_calendar_with_data(self):
        test_data = self.read_test_data('export_calendar_test_data.xlsx')
        for data in test_data:
            self.export_calendar(data)

    def export_calendar(self, data):
        self.command.execute(CommandChoices.CLICK, target="xpath=//a[@id='user-menu-toggle']")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/calendar/view.php?view=month")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/calendar/managesubscriptions.php")
        self.command.execute(CommandChoices.PAUSE, amount=2)
        self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/calendar/export.php")
        self.command.execute(CommandChoices.PAUSE, amount=2)

        if 'export_events_all' in data and data['export_events_all'].lower() == 'true':
            self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_events_exportevents_all']")
            self.command.execute(CommandChoices.PAUSE, amount=2)

        if 'period_timeperiod_weeknow' in data and data['period_timeperiod_weeknow'].lower() == 'true':
            self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_period_timeperiod_weeknow']")
            self.command.execute(CommandChoices.PAUSE, amount=2)

        if 'click_export' in data and data['click_export'].lower() == 'true':
            self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_export']")
            self.command.execute(CommandChoices.PAUSE, amount=2)

        if 'generate_url' in data and data['generate_url'].lower() == 'true':
            self.command.execute(CommandChoices.CLICK, target="xpath=//input[@id='id_generateurl']")
            self.command.execute(CommandChoices.PAUSE, amount=2)

        if 'assert_error_message' in data:
            error_message = self.driver.find_element(By.ID, "fgroup_id_error_period").text
            assert error_message == data['assert_error_message']
            self.command.execute(CommandChoices.PAUSE, amount=2)

        if 'open_home' in data and data['open_home'].lower() == 'true':
            self.command.execute(CommandChoices.OPEN, target="https://school.moodledemo.net/?redirect=0")
            self.command.execute(CommandChoices.PAUSE, amount=2)