
from selenium import webdriver
import time
import unittest
from framework.base_page import BasePage
from framework.login import LoginPage


class Sys_Management(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        LoginPage.login(self, 'ceshi03', '000000')



    # 一、总账初始
    # @unittest.skip
    def test01_booksStart(self):
        '''总账初始操作'''
        try:
            # 点击总账初始
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[7]/div/div/div/span").click()
            time.sleep(1)
            # 点击科目初始(政府)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[7]/ul/li[2]/div/div/div/div[1]/span").click()
            # 点击会计科目(1001 ceshi现金)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div/span[3]").click()
            # 点击试算平衡
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/ul/li[2]/span/button").click()
            time.sleep(1)
            # 点击取消
            self.driver.find_element_by_xpath("/html/body/div[87]/div[2]/div/div/div[3]/div/button[1]").click()
            # 点击导出
            # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/ul/li[6]/span/button").click()
            # 点击导入,再点击确定
            # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/ul/li[5]/span/button").click()
            # self.driver.find_element_by_xpath("/html/body/div[107]/div[2]/div/div/div/div/div[3]/button[2]/span").click()
            time.sleep(3)
        except Exception as e:
            print('错误信息:{}'.format(e))
            BasePage.takeScreenshot(self, '总账初始异常')

    # @unittest.skip
    # 二、总账启用
    def test02_booksusing(self):
        '''总账启用'''
        try:
            #点击总账初始
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[7]/div/div/div/span").click()
            #点击总账启用
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[7]/ul/li[1]/div/div/div/div[1]/span").click()
            # 点击下一步到试算平衡
            self.driver.find_element_by_xpath("/html/body/div[107]/div[2]/div/div/div[3]/div/button/span").click()
            # 点击下一步到启用成功
            self.driver.find_element_by_xpath("/html/body/div[107]/div[2]/div/div/div[3]/div/button[3]/span").click()
            # 点击关闭，总账启用窗口关闭
            self.driver.find_element_by_xpath("/html/body/div[107]/div[2]/div/div/div[3]/div/button/span").click()
        except Exception as e:
            print('错误信息:{}'.format(e))
            BasePage.takeScreenshot(self, '总账启用异常')

    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()