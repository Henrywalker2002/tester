import os
import pandas as pd
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .command import CommandChoices, Command
from .exceptions import (InvalidCommandException, AssertException,
                         InvalidTargetException, InvalidKeyChoicesException)


class Tool:
    def __init__(self, tc_path: str, driver_path: str = None):
        """
        tc_path: str, path to test case excel file
        driver_path: str, path to msedgedriver.exe
        """
        options = Options()
        path = os.path.abspath(__package__)
        excutable_path = driver_path if driver_path else f'{path}/msedgedriver.exe'
        service = Service(executable_path=excutable_path)
        self.driver = WebDriver(service=service, options=options)
        self.command = Command(self.driver)
        self.tc = pd.read_excel(tc_path, sheet_name=None, engine='openpyxl')
        self.tc_path = tc_path

    @staticmethod
    def generate_tc_file(tc_path: str):
        pass 
    
    @staticmethod
    def rename_test(df):
        for index, row in df.iterrows():
            if pd.isna(row['name']):
                df.loc[index, 'name'] = df.loc[index - 1, 'name']
        return df
    
    def handle_setup(self, sheetname: str, df: pd.DataFrame, tc_summary: pd.DataFrame, index : int):
        df_setup = self.tc.get(sheetname, None)
        if df_setup is None:
            df.loc[index, 'Result'] = 'Fail'
            df.loc[index, 'Error'] = 'No setup sheet found'
            tc_summary.loc[index, 'tc_name'] = sheetname
            tc_summary.loc[index, 'Result'] = 'Fail'
            tc_summary.loc[index, 'Error'] = 'No setup sheet found'
            return False, df, tc_summary
        for index, row in df_setup.iterrows():
            try:
                kwargs = row.to_dict()
                self.command.execute(
                    command=kwargs.pop('command', None), **kwargs)
            except Exception as e:
                df.loc[index, 'Result'] = 'Fail'
                df.loc[index, 'Error'] = str(e)
                tc_summary.loc[index, 'tc_name'] = sheetname
                tc_summary.loc[index, 'Result'] = 'Fail'
                tc_summary.loc[index, 'Error'] = str(e)
                return False, df, tc_summary
        return True, df, tc_summary
    
    def handle_tc(self, df: pd.DataFrame, tc_summary: pd.DataFrame) -> pd.DataFrame:
        df = self.rename_test(df)
        count = 0
        for tc_name in df['name'].unique():
            df_tc = df[df['name'] == tc_name]
            success = True
            for index, row in df_tc.iterrows():
                try:
                    kwargs = row.to_dict()
                    if kwargs.get('setup', False) and not pd.isna(kwargs.get('setup')):
                        res, df, tc_summary = self.handle_setup(kwargs.get('setup'), df, tc_summary, index)
                        if not res:
                            success = False
                            break
                    self.command.execute(
                        command=kwargs.pop('command', None), **kwargs)
                    df.loc[index, 'Result'] = 'Pass'
                    df.loc[index, 'Error'] = None
                    
                except Exception as e:
                    df.loc[index, 'Result'] = 'Fail'
                    df.loc[index, 'Error'] = str(e)
                    tc_summary.loc[count, 'tc_name'] = tc_name
                    tc_summary.loc[count, 'Result'] = 'Fail'
                    tc_summary.loc[count, 'Error'] = str(e)
                    count += 1
                    success = False
                    break
            if success:
                tc_summary.loc[count, 'tc_name'] = tc_name
                tc_summary.loc[count, 'Result'] = 'Pass'
                tc_summary.loc[count, 'Error'] = None
                count += 1
        return df, tc_summary

    def run(self):
        """
        Run all test cases in the test case excel file
        """
        tc_summary = pd.DataFrame()
        writer = pd.ExcelWriter('result.xlsx', engine='xlsxwriter')
        for sheetname, df in self.tc.items():
            if sheetname.startswith('setup'):
                continue
            df, tc_summary = self.handle_tc(df, tc_summary)
        for sheetname, df in self.tc.items():
            df.to_excel(writer, sheet_name=sheetname, index=False, engine='xlsxwriter')

        tc_summary.to_excel(writer, sheet_name='summary', index=False, engine='xlsxwriter', )
        writer.close()