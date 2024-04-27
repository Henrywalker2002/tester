from typing import Optional
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import unittest
import time 
import json 
import pandas as pd 
from auto_tool.command import Command, CommandChoices


class BaseTestCase(unittest.TestCase):
    
    driver: Optional[WebDriver] = None 
    command : Optional[Command] = None
    login_url = "https://school.moodledemo.net/login/index.php"
    redirect_url = "https://school.moodledemo.net/my/courses.php"
    data : list[dict] = []
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()    
        options = Options()
        service = Service(executable_path='./msedgedriver.exe')
        cls.driver = WebDriver(service=service, options=options)
        cls.command = Command(cls.driver)
    
    @classmethod
    def wait_until_url_is(self, url, timeout=30):
        start_time = time.time()
        while self.driver.current_url != url:
            if time.time() - start_time > timeout:
                raise Exception(f'Timed out waiting for URL to be {url}')
            time.sleep(0.5)
    
    @classmethod
    def login(self):
        self.driver.get(self.login_url)
        self.wait_until_url_is(self.redirect_url)
        cookies = self.driver.get_cookies()
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)
        if isinstance(cookies, list):
            for cookie in cookies:
                self.driver.add_cookie(cookie)
    
    @classmethod
    def login_with_account(self, username, password):
        self.command.execute(CommandChoices.OPEN, target = self.login_url)
        self.command.execute(CommandChoices.INPUT, value = {
            "username" : username,
            "password" : password
        })
        self.command.execute(CommandChoices.CLICK, target = "xpath=//button[@type='submit']")
        self.wait_until_url_is(self.redirect_url)
        cookies = self.driver.get_cookies()
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)
        if isinstance(cookies, list):
            for cookie in cookies:
                self.driver.add_cookie(cookie)
    
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()
    
    @classmethod 
    def load_data_xlsx(self, sheet_name, file_path = "./data.xlsx") -> list[dict]:
        df : pd.DataFrame = pd.read_excel(file_path, sheet_name = sheet_name)
        df.fillna('', inplace=True)
        lst = []
        for index, row in df.iterrows():
            lst.append(row.to_dict())
        return lst