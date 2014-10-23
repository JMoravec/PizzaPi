#!/usr/bin/env python

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from pizza_hut.constants import TIMEOUT

__author__ = 'Joshua Moravec'


class BasePage(object):
    """
    Base page type for all pages
    """

    def __init__(self, driver):
        self.driver = driver

    @property
    def title(self):
        WebDriverWait(self.driver, TIMEOUT).until(lambda e: self.driver.title)
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url

    def is_element_present(self, *locator):
        self.driver.implicitly_wait(0)
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            self.driver.implicitly_wait(TIMEOUT)

    def load(self, url):
        self.driver.get(url)
