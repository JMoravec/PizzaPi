#!/usr/bin/env python
"""
"""
from selenium import webdriver
from pizza_hut.MainPage import MainPage
from pizza_hut.constants import BASEURL

__author__ = 'Joshua Moravec'


driver = webdriver.Firefox()
driver.get(BASEURL)

mainPage = MainPage(driver)
mainPage.click_pizza_header_link()