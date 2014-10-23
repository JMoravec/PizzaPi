#!/usr/bin/env python
"""
"""
from selenium.webdriver.common.by import By
from pizza_hut.BasePage import BasePage
from pizza_hut.Pizza import Pizza

__author__ = 'Joshua Moravec'


class MainPage(BasePage):
    _url = "/"
    _title = "Pizza Hut - Pizza Coupons, Pizza Deals, Pizza Delivery, Order Pizza Online, Catering"
    _header_pizza_locator = (By.LINK_TEXT, "Pizza")

    def click_pizza_header_link(self):
        self.driver.find_element(*self._header_pizza_locator).click()
        return Pizza(self.driver)