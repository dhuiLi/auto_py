import string
import sys
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time
import os
import unittest
from framework.login import LoginPage
from framework.base_page import BasePage

class Sys_Management(unittest.TestCase):
    #打开浏览器
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()

    #系统管理操作
    def test_1_sysManageOperate(self):
        '''统管理操作'''
        try:
            LoginPage.login(self,'admin','admin')  #登录方法
            #点击系统管理下拉框
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[3]/div/i").click()
            time.sleep(2)
            #点击组织机构管理模块
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[3]/ul/li[1]/div/div/div/div[1]/span").click()
            #点击行政组织创建行政组织
            yuansu = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="orgTree"]/div[1]/div[2]/div[7]/div/span[2]/span')))
            yuansu.click()  #选择行政组织
            self.driver.implicitly_wait(10)
            #点击“新建下级”
            self.driver.find_element_by_css_selector("div:nth-child(1) > .va-toolbar-item > span").click()
            self.driver.implicitly_wait(10)
            seeds = string.digits
            random_str = random.choices(seeds, k=4)
            suiji = "".join(random_str)
            jigoudaima = '0'+ suiji
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div/form/div/div[2]/div[1]/div/div/div[1]/input").send_keys(jigoudaima)
            time.sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div/form/div/div[2]/div[2]/div/div/div[1]/input").send_keys('测试'+str(random.randint(1,10)))
            time.sleep(3)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div/form/div/div[3]/div/div/div/div[1]/input").send_keys("ceshi02")
            time.sleep(3)
            self.driver.find_element_by_css_selector("div:nth-child(4) > .va-toolbar-item > span").click()   #保存
            self.driver.implicitly_wait(10)

            self.driver.find_element_by_css_selector("div:nth-child(5) > .va-toolbar-item > span").click()  #删除
            time.sleep(2)
            self.driver.find_element_by_xpath('//input[contains(@placeholder,机构代码)]').send_keys(jigoudaima)
            self.driver.find_element_by_css_selector(".vertical-center-modal .ivu-btn-primary > span").click()
            time.sleep(2)

        except Exception as e:
            print('错误信息:{}'.format(e))
            # self.test_name = sys._getframe().f_code.co_name  # 获取当前调用函数的名字
            BasePage.takeScreenshot(self, '系统管理操作异常')




if __name__ == '__main__':
    unittest.main()


