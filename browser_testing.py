from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions as e
from selenium.webdriver.chrome.options import Options
from log_config import logging
from collections import OrderedDict
from operator import itemgetter
from selenium_config import *
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support.ui import Select
import json
import time
import unittest


LOGGER.setLevel(logging.WARNING)

URL_APP = "https://dancewithdeath.herokuapp.com/"

def get_browser_session(url):

    d = {}

    time.sleep(1)
    #deleting previous database entries
    driver.get(url + "api/delete_all")
    api_element = "/html/body/pre"
    driver.get(url)
    SELECT_INPUT = "/html/body/div[2]/div/div[2]/form/select"
    select(SELECT_INPUT, "March")
    hover_over("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[1]")
    select_hour = click("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[1]")
    deselect_hour = click("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[1]/button")
    #select same day different hour
    select_hour = click("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[2]")
    select(SELECT_INPUT, "February")
    hover_over("/html/body/div[2]/div/div[3]/div[4]/div[4]/div[1]")
    select_hour = click("/html/body/div[2]/div/div[3]/div[4]/div[4]/div[2]/div[1]")
    hover_over("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[1]")
    select_hour = click("/html/body/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[1]")
    hover_over("/html/body/div[2]/div/div[3]/div[5]/div[2]/div[1]")
    select_hour = click("/html/body/div[2]/div/div[3]/div[5]/div[2]/div[2]/div[8]/div")
    select(SELECT_INPUT, "April")
    hover_over("/html/body/div[2]/div/div[3]/div[3]/div[4]/div[1]")
    select_hour = click("/html/body/div[2]/div/div[3]/div[3]/div[4]/div[2]/div[2]")
    hover_over("/html/body/div[2]/div/div[3]/div[3]/div[7]/div[1]")
    select_hour = click("/html/body/div[2]/div/div[3]/div[3]/div[7]/div[2]/div[7]")
    hover_over("/html/body/div[2]/div/div[3]/div[2]/div[7]/div[1]")
    select_hour = click("/html/body/div[2]/div/div[3]/div[2]/div[7]/div[2]/div[4]")

    #the earliest expected date is February 4th 09:00:00 - 10:00
    d["next_scheduled_date"] = get_element_text("/html/body/div[3]/div")

    driver.get(url + "api/")

    d["scheduled_dates"] = get_element_text(api_element).replace("\n", "")
    logging.info(d)
    driver.quit()

    return d

browser_session_info = get_browser_session(URL_APP)

class TestModule(unittest.TestCase):

    def test_automation(self):
        '''function should fail on wrong type inputs'''
        self.assertIn('next_scheduled_date', browser_session_info)
        self.assertIn('scheduled_dates', browser_session_info)
        self.assertNotEqual("NEXT DATE SCHEDULED: 10 February 9:00 - 10:00", browser_session_info["next_scheduled_date"])
        self.assertNotEqual("NEXT DATE SCHEDULED: 17 February 9:00 - 10:00", browser_session_info["next_scheduled_date"])
        self.assertNotEqual( '["10/03/2022/10:00:00 - 11:00:00","17/02/2022/09:00:00 - 10:00:00","04/02/2022/09:00:00 - 10:00:00","22/02/2022/16:00:00 - 17:00:00","07/04/2022/10:00:00 - 11:00:00","10/04/2022/15:00:00 - 16:00:00","03/04/2022/12:00:00 - 13:00:00"]',
                             browser_session_info["next_scheduled_date"])
        self.assertEqual("NEXT DATE SCHEDULED: 4 February 9:00 - 10:00", browser_session_info["next_scheduled_date"])
        self.assertEqual('["04/03/2022/10:00:00 - 11:00:00","17/02/2022/09:00:00 - 10:00:00","04/02/2022/09:00:00 - 10:00:00","22/02/2022/16:00:00 - 17:00:00","07/04/2022/10:00:00 - 11:00:00","10/04/2022/15:00:00 - 16:00:00","03/04/2022/12:00:00 - 13:00:00"]',
                         browser_session_info["scheduled_dates"])

if __name__ == "__main__":
    unittest.main()

