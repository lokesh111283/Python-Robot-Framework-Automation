import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup","getdata")
class Baseclass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
    def verify_if_login_locator_available(self,var_in_conf):
        print(var_in_conf)
        element =WebDriverWait(self.driver,10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, var_in_conf)))

    def verify_if_logout_locator_available(self,var_sign_out_conf):
        print(var_sign_out_conf)
        element =WebDriverWait(self.driver,20).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, var_sign_out_conf)))



