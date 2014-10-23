#!/usr/bin/env python
"""
"""
from pizza_hut.BasePage import BasePage
from pizza_hut.constants import BASEURL

__author__ = 'Joshua Moravec'


class Pizza(BasePage):
    _url = BASEURL + "/site/menu/pizza"

    def __init__(self, driver):
        super().__init__(driver)
        if self.current_url != self._url:
            self.load(self._url)

