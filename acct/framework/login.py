import time
import unittest
from selenium import webdriver


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def login(self,username,password):
        url = "http://172.16.20.52:9002/"
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[3]/div/div/div/div[3]/div/form/div[1]/div/div[1]/input").send_keys(username)
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[3]/div/div/div/div[3]/div/form/div[2]/div/div/input").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div[3]/div/div/div/div[3]/div/form/div[3]/div/button").click()
        self.driver.implicitly_wait(10)

