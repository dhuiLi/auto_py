
import random
from selenium import webdriver
import time
import unittest
from framework.base_page import BasePage
from framework.login import LoginPage


class Sys_Management(unittest.TestCase):

    # 打开浏览器
    @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.implicitly_wait(30)
    #     cls.driver.maximize_window()
    #     LoginPage.login(cls, 'ceshi03', '000000')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        LoginPage.login(self, 'ceshi03', '000000')



    # 一、科目管理
    # @unittest.skip
    def test01_accountPeriod(self):
        '''科目管理操作'''
        try:
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/div/div/div/span").click()
            time.sleep(3)
            # 一、选择科目管理模块
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/ul/li[4]/div/div/div/div[1]/span").click()
            # 选择会计科目，资产类
            time.sleep(3)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[5]").click()
            # 点击新增
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/ul/li[1]/span/button").click()
            time.sleep(2)
            # 新增科目
            # 代码
            dm = self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div[1]/div/div/input")
            dm.click()
            dm.clear()
            time.sleep(1)
            num = random.randint(10,99)
            dm.send_keys('10'+str(num))
            # 名称
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div[2]/div/div/input").send_keys(
                "ceshi现金"+str(num))
            # 科目属性
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/span").click()
            # 选择普通科目
            self.driver.find_element_by_xpath("/html/body/div[85]/ul[2]/li[1]").click()
            time.sleep(1)
            # 点击启用往来
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div[4]/div/label[2]/span[1]/input").click()
            # 明细核算要素，启用辅助项的往来单位
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/form/div[2]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[1]/div/label/span/input").click()
            # 点击保存
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/div/button[3]/span").click()
            time.sleep(3)
        except Exception as e:
            print('错误信息:{}'.format(e))
            BasePage.takeScreenshot(self, '科目管理异常')

    # @unittest.skip
    # 二、基础数据_云核算
    def test02_accountPeriod(self):
        '''基础数据_云核算'''
        try:
            # 基础数据_云核算
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/div/div/div/span").click()
            #点击基础数据_云核算模块
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/ul/li[3]/div/div/div/div[1]/span").click()
            time.sleep(2)
            #创建定义
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[1]/button/span").click()
            #输入标识
            biaoshi = random.randint(10,50)
            self.driver.find_element_by_css_selector("body > div:nth-child(95) > div.ivu-modal-wrap.operate_define > div > div > div.ivu-modal-body > form > div:nth-child(1) > div > div > input").send_keys("MD_ceshi"+str(biaoshi))
            #输入名称
            self.driver.find_element_by_css_selector("body > div:nth-child(95) > div.ivu-modal-wrap.operate_define > div > div > div.ivu-modal-body > form > div:nth-child(2) > div > div > input").send_keys("测试"+str(biaoshi))
            #点击确定
            self.driver.find_element_by_xpath("/html/body/div[87]/div[2]/div/div/div[3]/div/button[2]/span").click()
            time.sleep(3)
        except Exception as e:
            print('错误信息:{}'.format(e))
            BasePage.takeScreenshot(self, '云核算异常')

    # 三、项目
    # @unittest.skip
    def test03_accountPeriod(self):
        '''项目'''
        try:
            #点击基础数据
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/div/div/div/span").click()
            time.sleep(2)
            #点击项目
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/ul/li[1]/div/div/div/div[1]/span").click()
            time.sleep(2)
            #点击新增
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[1]/button/span").click()
            time.sleep(1)
            #项目信息，代码
            xmxx = random.randint(10,99)
            self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input").send_keys("100"+str(xmxx))
            time.sleep(1)
            #名称
            self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[2]/div/div/input").send_keys("cehsi项目")
            time.sleep(1)
            #点击确定
            self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[3]/div/button[2]/span").click()
            time.sleep(3)
        except Exception as e:
            print('错误信息:{}'.format(e))
            BasePage.takeScreenshot(self, '项目异常')

    # 四、往来单位
    def test04_accountPeriod(self):
        '''往来单位'''
        try:
            # 点击基础数据
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/div/div/div/span").click()
            time.sleep(2)
            # 点击往来单位
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/ul/li[2]/div/div/div/div[1]/span").click()
            # 点击新增
            time.sleep(2)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[1]/button/span").click()
            # 清空输入框
            dm1 = self.driver.find_element_by_xpath(
                "/html/body/div[86]/div[2]/div/div/div[2]/form/div[1]/div/div/input")
            dm1.clear()
            # 往来单位信息,代码
            suiji = random.randint(10,200)
            self.driver.find_element_by_xpath(
                "/html/body/div[86]/div[2]/div/div/div[2]/form/div[1]/div/div/input").send_keys(suiji)
            # 名称
            self.driver.find_element_by_xpath(
                "/html/body/div[86]/div[2]/div/div/div[2]/form/div[2]/div/div/div[1]/input").send_keys(
                "ceshi项目"+str(suiji))
            time.sleep(1)
            # 点击确定
            self.driver.find_element_by_xpath(
                "/html/body/div[86]/div[2]/div/div/div[3]/div/button[2]/span").click()
            time.sleep(1)
        except Exception as e:
            print('错误信息:{}'.format(e))
            BasePage.takeScreenshot(self, '往来单位异常')

    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
if __name__ == '__main__':
    unittest.main()