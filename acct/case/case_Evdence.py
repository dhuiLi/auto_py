
from selenium import webdriver
import time
import unittest

from selenium.webdriver import ActionChains


from framework.base_page import BasePage
from framework.login import LoginPage


class Sys_Management(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        LoginPage.login(self, 'ceshi03', '000000')



    # 一、凭证录入
    # @unittest.skip
    def test01_evdenceInput(self):
    #     '''凭证录入操作'''
        try:
            # 点击凭证
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[8]/div").click()

            # 1.点击凭证录入
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[8]/ul/li[1]/div/div/div/div[1]/span").click()
            time.sleep(3)
            #凭证字选择
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div/i").click()
            time.sleep(1)
            #选择记
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/div[2]/ul[2]/li[1]").click()
            #录入“记账凭证”的信息
            #1)编写摘要
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[5]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div[1]").click()
            time.sleep(1)
            a = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[5]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div[1]/div[1]/div")
            ActionChains(self.driver).double_click(a).perform()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[5]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div[1]/span/div/div/input").send_keys("测试费用001")
            time.sleep(1)
            #2)编写科目
            b = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[5]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div/div/div[2]/div")
            ActionChains(self.driver).double_click(b).perform()
            #点击科目
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[5]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div/div/span/div/button/span").click()
            time.sleep(1)
            #科目搜索,选择资产类，1042
            self.driver.find_element_by_xpath("/html/body/div[101]/div/div[2]/div[1]/div/input").send_keys("1042")
            #点击搜索
            self.driver.find_element_by_xpath("/html/body/div[101]/div/div[2]/div[1]/div/i[1]").click()
            #选中1042
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[101]/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[5]/div/span[3]").click()
            #点击确定
            self.driver.find_element_by_xpath("/html/body/div[101]/div/div[3]/div/button[2]/span").click()
            time.sleep(2)
            #填写往来单位
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[5]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div/div/span/div/div/input").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[101]/div/div[1]/div/ul/li").click()
            self.driver.find_element_by_xpath("/html/body/div[101]/div/div[1]/div/div/div/div[2]/div[1]/span/div[2]/div/span/i").click()
            #往来单位输入框搜索
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[103]/div/div[2]/div[1]/div/input").send_keys("11")
            #点击搜索
            self.driver.find_element_by_xpath("/html/body/div[103]/div/div[2]/div[1]/div/i[1]").click()
            #选择11得往来单位
            self.driver.find_element_by_xpath("/html/body/div[103]/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div/span[3]").click()
            #点击确定
            self.driver.find_element_by_xpath("/html/body/div[103]/div/div[3]/div/button[2]/span").click()
            #填写业务编号
            self.driver.find_element_by_xpath("/html/body/div[101]/div/div[1]/div/div/div/div[2]/div[2]/div/input").send_keys("001")
            #选择业务日期
            self.driver.find_element_by_xpath("/html/body/div[101]/div/div[1]/div/div/div/div[2]/div[3]/div/div/div/input").click()
            self.driver.find_element_by_xpath("/html/body/div[102]/div/div/div/div[1]/span[2]/i").click()
            self.driver.find_element_by_xpath("/html/body/div[102]/div/div/div/div[2]/div/span[19]/em").click()

            #3)借方，双击
            c = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[5]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[4]/div/div/div/div[1]")
            ActionChains(self.driver).double_click(c).perform()
            #输入1000
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[5]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[4]/div/div/div/div/input").send_keys("1000")
            time.sleep(1)
            #4)点击暂存
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[5]/span/button/span").click()
            #点击保存
            # #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[4]/span/button").click()


            #点击菜单
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/span/button/span/span").click()
            time.sleep(2)
            #选择文件
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/span/div/div/div[1]/div/span/div/div[3]").click()
            time.sleep(2)
            #选择暂存凭证
            self.driver.find_element_by_xpath("/html/body/div[114]/div/div[2]/div/span/div[2]/div[2]/span").click()
            #选择常用凭证
            #self.driver.find_element_by_xpath("/html/body/div[101]/div/div[3]/div/span/div[2]/div[2]/span").click()
            # 选择场景模板
            # self.driver.find_element_by_xpath("/html/body/div[101]/div/div[4]/div[1]/span/div[2]/div[2]/span").click()
            # 保存常用凭证
            # self.driver.find_element_by_xpath("/html/body/div[101]/div/div[7]/div/span/div[2]/div[2]/span").click()
            # 保存场景模板
            # self.driver.find_element_by_xpath("/html/body/div[101]/div/div[8]/div[1]/span/div[2]/div[2]/span").click()

        except Exception as e:
            print('错误信息:{}'.format(e))
            BasePage.takeScreenshot(self, '凭证录入异常')

    # @unittest.skip
    # 二、凭证管理
    def test02_evdenceMana(self):
        '''凭证管理'''
        try:
            # 点击凭证
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[8]/div").click()

            # 2.凭证管理
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[8]/ul/li[2]/div/div/div/div[1]/span").click()
            time.sleep(3)
            # 1)录入选中一条凭证
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span").click()
            # 点击修改
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/ul/li[2]/span/button/span").click()
            # 点击删除
            # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/ul/li[3]/span/button/span").click()
            # 点击确定
            # self.driver.find_element_by_xpath("/html/body/div[126]/div[2]/div/div/div/div/div[3]/button[2]").click()
            # 修改，摘要信息
            time.sleep(2)
            d = self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[5]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div[1]")
            ActionChains(self.driver).double_click(d).perform()
            # 清空摘要并重新输入信息
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[5]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div[1]/span/div[2]/div/input").clear()
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[5]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div[1]/span/div[2]/div/input").send_keys(
                "测试费用001修改")
            # 暂存
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/ul/li[5]/span/button").click()
            time.sleep(2)
            # 点击返回
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/i").click()
            time.sleep(1)

            # 2）点击上方的审核
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div[1]/div[3]/span").click()
            # 选择序号4
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[3]/table/tbody/tr[4]/td[1]/div/label/span/span").click()
            time.sleep(1)
            # 点击审核
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/ul/li[1]/span/button/span").click()

            # 提示信息中点击关闭
            self.driver.find_element_by_xpath("/html/body/div[91]/div[2]/div/div/div[3]/div/button/span").click()
            # 记账凭证切换已审核的
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/form/div[1]/div/div/div[1]/div/i").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/form/div[1]/div/div/div[2]/ul[2]/li[2]").click()
            time.sleep(1)
            # 选中一个凭证
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[3]/table/tbody/tr/td[1]/div/label/span/span").click()
            # 取消审核
            # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/ul/li[2]/span/button/span").click()
            # 提示信息点击关闭
            # self.driver.find_element_by_xpath("/html/body/div[91]/div[2]/div/div/div[3]/div/button/span").click()

            # 3）点击上方的记账
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[5]/span").click()
            # 选择序号4
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[3]/table/tbody/tr[4]/td[1]/div/label/span/span").click()
            time.sleep(1)
            # 选择记账
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/ul/li[1]/span/button/span").click()
            # 提示信息点击关闭
            self.driver.find_element_by_xpath("/html/body/div[91]/div[2]/div/div/div[3]/div/button/span").click()
            # 记账凭证切换已记账的
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/form/div[1]/div/div/div[1]/div/i").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/form/div[1]/div/div/div[2]/ul[2]/li[2]").click()
            # 选择序号1
            time.sleep(2)
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[3]/table/tbody/tr/td[1]/div/label/span/span").click()
            # 取消记账
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/ul/li[2]/span/button/span").click()
            # 点击确定
            self.driver.find_element_by_xpath("/html/body/div[128]/div[2]/div/div/div/div/div[3]/button[2]").click()
            # 关闭
            self.driver.find_element_by_xpath("/html/body/div[91]/div[2]/div/div/div[3]/div/button/span").click()

        except Exception as e:
            print('错误信息:{}'.format(e))
            BasePage.takeScreenshot(self, '凭证管理异常')


    #三、凭证汇总
    def test03_evdenceCollect(self):
        '''凭证汇总操作'''
        try:

           # 点击凭证
           self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[8]/div").click()
        # 点击凭证汇总
           self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[8]/ul/li[3]/div/div/div/div[1]/span").click()
           time.sleep(3)
        # 凭证字选择
           self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div/div/form/div/div[2]/div/div/div[1]/div/i").click()
           self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div/div/form/div/div[2]/div/div/div[2]/ul[2]/li[2]").click()
        # 点击查询结果
           time.sleep(1)
           #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div/div/div/button[1]/span").click()
           #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div/div/div/button[1]/span").click()
           #time.sleep(3)
        # 保存为方案
           self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div/div/div/button[2]/span").click()
           self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div/div/div/button[2]/span").click()
        # 清空方案名称输入框
           self.driver.find_element_by_xpath("/html/body/div[94]/div[2]/div/div/div[2]/form/div/div/div/input").clear()
        # 填写新的方案名称
           self.driver.find_element_by_xpath("/html/body/div[94]/div[2]/div/div/div[2]/form/div/div/div/input").send_keys("测试方案123")
        # 点击确认
           self.driver.find_element_by_xpath("/html/body/div[94]/div[2]/div/div/div[3]/div/button[2]/span").click()
           time.sleep(2)
        #点击取消
           #self.driver.find_element_by_xpath("/html/body/div[94]/div[2]/div/div/div[3]/div/button[1]/span").click()

        except Exception as e:
            print('错误信息:{}'.format(e))
            BasePage.takeScreenshot(self, '凭证汇总异常')


    #四、序时账
    def test04_evdenceJoumal(self):
        '''序时账操作'''
        try:
            # 点击凭证
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[8]/div").click()
            # 点击序时账
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[8]/ul/li[4]/div/div/div/div[1]/span").click()
            time.sleep(3)
            # 日期范围
            # 开始时间
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/form/div[1]/div[1]/div[2]/div[1]/div[1]/div/input").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/form/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/span[5]/em").click()
            time.sleep(1)
            # 结束时间
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/form/div[1]/div[1]/div[2]/div[2]/div[1]/div/input").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/form/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div/div[1]/span[5]/i").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/form/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/span[12]/em").click()
            time.sleep(1)
            # 输入摘要搜索条件
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/form/div[1]/div[2]/div[2]/div/input").send_keys("差旅费")
            time.sleep(2)
            # 点击查询结果按钮
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/form/div[2]/div[2]/button[1]/span").click()
            time.sleep(3)
            # 保存为方案
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/form/div[2]/div[2]/button[2]/span").click()
            # 清空
            #self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div/div/div/input").clear()
            #self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div/div/div/input").send_keys("序时账测试001")
            # 确认
            #self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[3]/div/button[2]/span").click()

        except Exception as e:
            print('错误信息:{}'.format(e))
            BasePage.takeScreenshot(self, '序时账异常')


    #五、常用凭证
    def test05_evdenceCommon(self):
        '''常用凭证操作'''
        try:
            # 点击凭证
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[8]/div").click()
            # 点击常用凭证
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[8]/ul/li[5]/div/div/div/div[1]/span").click()
            self.driver.implicitly_wait(10)
            # 点击新增
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/ul/li[1]/span/button").click()
            # 选择凭证字
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/i").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[1]/div/div[1]/div[2]/ul[2]/li[1]").click()
            # 选择分组
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/i").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/ul[2]/li").click()
            time.sleep(1)
            # 名称
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[1]/div/div[3]/input").send_keys("常用凭证测试00123")
            # 录入常用凭证
            # 摘要
            e = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div[1]/div[1]/div")
            ActionChains(self.driver).double_click(e).perform()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div[1]/span/div[2]/div/input").send_keys("测试001")
            # 科目
            f = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div/div/div[2]/div")
            ActionChains(self.driver).double_click(f).perform()
            # 点击科目
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div/div/span/div/button/span").click()
            # 搜索
            self.driver.find_element_by_xpath("/html/body/div[90]/div/div[2]/div[1]/div/input").send_keys("1071")
            # 点击搜索按钮
            self.driver.find_element_by_xpath("/html/body/div[90]/div/div[2]/div[1]/div/i[1]").click()
            # 选中
            self.driver.find_element_by_xpath("/html/body/div[90]/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[7]/div/span[3]").click()
            # 确定
            self.driver.find_element_by_xpath("/html/body/div[90]/div/div[3]/div/button[2]/span").click()
            # 借方输入
            g = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[4]/div/div/div/div[1]")
            ActionChains(self.driver).double_click(g).perform()
            # 输入金额
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[4]/div/div/div/div/input").send_keys("1000")
            time.sleep(1)
            # 保存
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[1]/ul/li/span/button").click()

            # 导入
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/ul/li[5]/span/button").click()
            # 搜索框查询
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[3]/div/div/div[1]/div/input").send_keys("002")
            # 选中进行复制
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[1]/div/label/span/span").click()
            # 点击复制按钮
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/ul/li[4]/span/button").click()
            # 点击删除按钮
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/ul/li[3]/span/button").click()
            # 点击修改
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/ul/li[2]/span/button").click()




        except Exception as e:
            print('错误信息:{}'.format(e))
            BasePage.takeScreenshot(self, '常用凭证异常')



    #六、场景库
    def test06_evdeceScene(self):
        '''场景库操作'''
        try:
            # 点击凭证
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[8]/div").click()
            # 点击场景库
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[8]/ul/li[6]/div/div/div/div[1]/span").click()
            time.sleep(3)
            # 切换模板
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div/i").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]/ul[2]/li[1]").click()
            # 点击默认分组
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/span[3]").click()
            # 搜索框搜索数据
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[3]/div/div[1]/div/input").send_keys("1")
            # 勾选场景库凭证
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/table/tbody/tr/td[1]/div/label/span/span").click()
            # 导出,系统报系统异常
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/ul/li[6]/span/button").click()
            # 导入
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/ul/li[5]/span/button").click()
            # 新建场景
            # 点击新建场景
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/ul/li[1]/span/button").click()
            # 场景分组
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/i").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/ul[2]/li").click()
            time.sleep(1)
            # 输入场景名称
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[3]/input").send_keys(
                "场景库测试003")
            # 录入摘要
            h = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div[1]/div[1]/div")
            ActionChains(self.driver).double_click(h).perform()
            # 输入摘要
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/div[1]/span/div[2]/div/input").send_keys("测试001")
            # 科目
            i = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div/div/div[2]/div")
            ActionChains(self.driver).double_click(i).perform()
            # 点击科目
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div/div/span/div/button/span").click()
            # 科目选择
            self.driver.find_element_by_xpath("/html/body/div[91]/div/div[2]/div[1]/div/input").send_keys("6001")
            # 点击搜索
            self.driver.find_element_by_xpath("/html/body/div[91]/div/div[2]/div[1]/div/i[1]").click()
            # 选择6001
            self.driver.find_element_by_xpath("/html/body/div[91]/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/span[3]").click()
            # 点击确定
            self.driver.find_element_by_xpath("/html/body/div[91]/div/div[3]/div/button[2]/span").click()
            # 输入借方信息
            g = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[4]/div/div/div/div[1]")
            ActionChains(self.driver).double_click(g).perform()
            # 输入金额
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[4]/div/div/div/div/input").send_keys("2000")

            # 输入第二行数据
            # 摘要
            h = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/div[1]/div[1]/div")
            ActionChains(self.driver).double_click(h).perform()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/div[1]/span/div[2]/div/input").send_keys("测试002")
            # 科目
            i = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/div/div[2]/div")
            ActionChains(self.driver).double_click(i).perform()
            # 点击科目
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[3]/div/div/div/span/div/button/span").click()
            # 搜索输入框
            self.driver.find_element_by_xpath("/html/body/div[91]/div/div[2]/div[1]/div/input").send_keys("6001")
            # 点击搜索
            self.driver.find_element_by_xpath("/html/body/div[91]/div/div[2]/div[1]/div/i[1]").click()
            # 选择6001
            self.driver.find_element_by_xpath("/html/body/div[91]/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/span[3]").click()
            # 点击确定
            self.driver.find_element_by_xpath("/html/body/div[91]/div/div[3]/div/button[2]/span").click()
            time.sleep(2)
            # 借方输入
            j = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[5]/div/div/div/div[1]")
            ActionChains(self.driver).double_click(j).perform()
            # 输入金额
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[5]/div/div/div/div/input").send_keys("2000")
            # 点击保存
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/ul/li/span/button").click()
            time.sleep(2)
            # 点击删除场景
            # 选中场景
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/table/tbody/tr[2]/td[1]/div/label/span/span").click()
            # 删除场景
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/ul/li[3]/span/button").click()
            # 点击确认
            self.driver.find_element_by_xpath("/html/body/div[91]/div[2]/div/div/div/div/div[3]/button[2]").click()
            # 点击取消
            #self.driver.find_element_by_xpath("/html/body/div[89]/div[2]/div/div/div/div/div[3]/button[1]").click()

            # 修改场景
            # 选中场景
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/table/tbody/tr[2]/td[1]/div/label/span/span").click()
            # 选中修改场景
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/ul/li[2]/span/button").click()
            time.sleep(1)
            # 修改摘要
            #k = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/div[1]/div[1]/div")
            #ActionChains(self.driver).double_click(k).perform()
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/div[1]/span/div[2]/div/input").clear()
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/div[1]/span/div[2]/div/input").send_keys("测试002修改")
            # 保存
            #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/ul/li/span/button").click()



        except Exception as e:
            print('错误信息:{}'.format(e))
            BasePage.takeScreenshot(self, '场景库异常')



    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()