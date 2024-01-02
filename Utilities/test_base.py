import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import inspect
import os


class TestBase:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_element(self, locator, timeout=20):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_interactable(self, locator, timeout=20):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        return element

    @staticmethod
    def get_logger(self):
        calling_function_name = inspect.stack()[1][3]
        logger = logging.getLogger(calling_function_name)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        report_dir = os.path.join(os.getcwd(), "Reports")
        log_dir = os.path.join(report_dir, "Logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file_path = os.path.join(log_dir, "logfile.log")

        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger