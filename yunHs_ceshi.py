from selenium import webdriver
import time
import yaml
import os
from selenium.webdriver.common.keys import Keys


class keYan_Ceshi():

    def readYaml(self):
        #读取yaml文件
        testdir = os.path.dirname(os.path.dirname(__file__))
        test_dir = os.path.join(testdir, 'D:/安装包/pycharmJob/zidong01/ke01/common.yaml')
        a = open(test_dir, 'r', encoding='utf-8')
        b = a.read()
        c = yaml.load(b)
        return c



    #打开浏览器
    def openBrower(self):
        y = keYan_Ceshi
        yy = y.readYaml(y)

        self.driver = webdriver.Chrome()
        url = yy["hsurl"]
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    #关闭浏览器
    #def closeBrower(self):
     #   self.driver.quit()
    #登录
    def signIn(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div/div[3]/div/form/div[1]/div/div[1]/input").send_keys("admin")
        self.driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div/div[3]/div/form/div[2]/div/div/input").send_keys("admin")
        self.driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div/div[3]/div/form/div[3]/div/button").click()
        self.driver.implicitly_wait(3)
    #系统管理操作
    def sysManageOperate(self):
        #点击系统管理下拉框
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[3]/div/i").click()
        time.sleep(2)

        #一、点击组织机构管理模块
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[3]/ul/li[1]/div/div/div/div[1]/span").click()
        self.driver.implicitly_wait(3)
        #点击行政组织创建行政组织
        #选择行政组织的
        self.driver.find_element_by_css_selector(".el-tree-node:nth-child(7) .custom-tree-node > span").click()
        #点击“新建下级”
        self.driver.find_element_by_css_selector("div:nth-child(1) > .va-toolbar-item > span").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div/form/div/div[2]/div[1]/div/div/div[1]/input").send_keys("00802")
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div/form/div/div[2]/div[2]/div/div/div[1]/input").send_keys("测试02")
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div/form/div/div[3]/div/div/div/div[1]/input").send_keys("ceshi02")
        time.sleep(1)
        #保存
        self.driver.find_element_by_css_selector("div:nth-child(4) > .va-toolbar-item > span").click()
        time.sleep(2)
        # #删除
        # self.driver.find_element_by_css_selector("div:nth-child(5) > .va-toolbar-item > span").click()
        # self.driver.find_element_by_xpath("/html/body/div[87]/div[2]/div/div/div[2]/form/div/div/div/input").send_keys("00802")
        # self.driver.find_element_by_css_selector(".vertical-center-modal .ivu-btn-primary > span").click()
        # #切换行政组织，关联创建
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/i").click()
        # time.sleep(2)
        # #选择财务组织
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/ul[2]/li[2]").click()
        # self.driver.implicitly_wait(3)
        # #关联创建
        # self.driver.find_element_by_css_selector("div:nth-child(1) > .va-toolbar-item > span").click()
        # time.sleep(2)
        # #选择行政组织并确定
        # self.driver.find_element_by_xpath("/html/body/div[89]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[7]/div[1]/span[1]").click()
        # self.driver.implicitly_wait(2)
        # self.driver.find_element_by_xpath("/html/body/div[89]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[7]/div[2]/div[2]/div/label/span").click()
        # self.driver.find_element_by_xpath("/html/body/div[89]/div[2]/div/div/div[3]/button[2]").click()

        # #二、用户管理模块
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[3]/ul/li[2]/div/div/div/div[1]/span").click()
        # #点击“测试”行政组织
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div[7]/div[1]/span[1]").click()
        # time.sleep(2)
        # #选中新建的“测试02”
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div[7]/div[2]/div[2]/div/span[2]").click()
        # #点击新建用户
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div[1]/div/div[1]/div[1]/button").click()
        # time.sleep(1)
        # #填写基本信息
        # #登录名
        # self.driver.find_element_by_xpath("/html/body/div[85]/div[2]/div/div/div[2]/div/form/div[1]/div/div/div[1]/div/input").send_keys("ceshi02")
        # #用户名
        # self.driver.find_element_by_xpath("/html/body/div[85]/div[2]/div/div/div[2]/div/form/div[2]/div/div/div[1]/div/input").send_keys("测试02")
        # #密码
        # self.driver.find_element_by_xpath("/html/body/div[85]/div[2]/div/div/div[2]/div/form/div[3]/div/div/div[1]/div/input").send_keys("000000")
        # #确认密码
        # self.driver.find_element_by_xpath("/html/body/div[85]/div[2]/div/div/div[2]/div/form/div[4]/div/div[1]/div[1]/div/input").send_keys("000000")
        # #取消“下次登录需要修改密码”
        # self.driver.find_element_by_xpath("/html/body/div[85]/div[2]/div/div/div[2]/div/form/div[9]/div/label/span/input").click()
        # #点击确定
        # self.driver.find_element_by_xpath("/html/body/div[85]/div[2]/div/div/div[3]/button[2]").click()
        #选择行政组织
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div[7]/div[2]/div[2]/div").click()
        # #选择授权
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/span/a[2]").click()
        # #设置用户权限，切换到功能资源
        # self.driver.find_element_by_xpath("/html/body/div[89]/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/i").click()
        # self.driver.implicitly_wait(2)
        # #选择功能资源
        # self.driver.find_element_by_xpath("/html/body/div[89]/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/ul[2]/li[4]").click()
        # time.sleep(1)
        # #勾选功能菜单，访问
        # self.driver.find_element_by_xpath("/html/body/div[89]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div[3]/div/div/div/div[1]/div[2]/table/tbody/tr[2]/td[3]/div/label/span/input").click()
        # #点击保存
        # self.driver.find_element_by_xpath("/html/body/div[89]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/button/span").click()


        #三、角色管理
        #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[3]/ul/li[3]/div/div/div/div[1]/span").click()

        #账簿管理
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[4]/div/i").click()
        # time.sleep(1)
        # #1)会计期间方案
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[4]/ul/li[2]/div/div/div/div[1]/span").click()
        # #新增
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div[1]/button/span").click()
        # #点击并输入代码
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[1]/div/div/input").click()
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[1]/div/div/input").send_keys("03")
        # #点击并输入名称
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[2]/div/div[1]/input").click()
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[2]/div/div[1]/input").send_keys("ceshi03")
        # #启用年份
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[3]/div/div/input").clear()
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[3]/div/div/input").send_keys("2018")
        # #启动调整期
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[4]/div/span").click()
        # #点击确定按钮
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[3]/div/button[2]").click()
        #
        #
        # #2)会计期间
        # #点击会计期间
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[4]/ul/li[3]/div/div/div/div[1]/span").click()
        # time.sleep(1)
        # #点击新增
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/button").click()


        # #3)科目方案
        # #点击科目方案
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[4]/ul/li[1]/div/div/div/div[1]/span").click()
        # #点击新增按钮
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div[1]/button").click()
        # self.driver.implicitly_wait(2)
        # #输入科目方案编码
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input").send_keys("03")
        # #输入科目方案名称
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[2]/div/div/input").send_keys("测试科目方案")
        # #输入科目编码规则
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[3]/div/div/input").send_keys("4111111")
        # #启用双体系
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[5]/div/span").click()
        # #点击确定
        # self.driver.find_element_by_xpath("/html/body/div[128]/div[2]/div/div/div/div/div[3]/button[2]/span").click()
        # #设置平衡公式
        # #科目类型编码1
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[1]/td[2]/div/div/input").send_keys("001")
        # #科目类型名称
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[1]/td[3]/div/div").click()
        # #选择资产类
        # self.driver.find_element_by_xpath("/html/body/div[88]/ul[2]/li[1]").click()
        # #科目类型编码2
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[2]/td[2]/div/div/input").send_keys("002")
        # #科目类型名称
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[2]/td[3]/div/div").click()
        # #选择负债类
        # self.driver.find_element_by_xpath("/html/body/div[92]/ul[2]/li[2]").click()
        # #选择余额方向
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[2]/td[4]/div/div/div").click()
        # #选择贷方
        # #self.driver.find_element_by_xpath("/html/body/div[93]/ul[2]/li[2]").click()
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[3]/td[1]/div/div").click()
        # #科目类型编码3
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[3]/td[2]/div/div/input").send_keys("003")
        # #科目类型名称
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[3]/td[3]/div/div").click()
        # #选择成本类
        # self.driver.find_element_by_xpath("/html/body/div[96]/ul[2]/li[4]").click()
        # #选择余额方向
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[3]/td[4]/div/div/div").click()
        # #选择贷方
        # self.driver.find_element_by_xpath("/html/body/div[97]/ul[2]/li[2]").click()
        # #选择平衡公式位置
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[3]/td[5]/div/div").click()
        # #选择等式右侧
        # self.driver.find_element_by_xpath("/html/body/div[98]/ul[2]/li[2]").click()
        #
        # #点击第4行
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[4]/td[1]/div").click()
        # #删除第4行
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[4]/td[8]/div/a[3]").click()
        # #删除第4行的第五行数据
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[7]/div[3]/table/tbody/tr[4]/td[8]/div/a[3]").click()
        #
        # #点击确定按钮
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[3]/div/button[2]").click()


        # #4)创建账簿管理
        # #选择账簿管理模块
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[4]/ul/li[4]/div/div/div/div[1]/span").click()
        # time.sleep(2)
        # #从账簿列表选择一个账簿，测试账簿
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div/ul/li/ul[9]/li/span[2]").click()
        # #点击新增
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div[1]/button/span").click()
        # self.driver.implicitly_wait(2)
        # #新增账簿
        # #代码
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[1]/div/div/input").send_keys("0901")
        # #名称
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[2]/div/div/input").send_keys("测试账簿01")
        # #本位币
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[3]/div/div/div[1]").click()
        # #选择人民币
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[3]/div/div/div[2]/ul[2]/li[1]").click()
        # #选择科目方案
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[4]/div/div/div[1]/div/span").click()
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[4]/div/div/div[2]/ul[2]/li[3]").click()
        # #选择会计期间方案
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[5]/div/div/div[1]/div/span").click()
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/form/div[5]/div/div/div[2]/ul[2]/li[1]").click()
        #
        # #点击确定
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[3]/div/button[2]/span").click()

        # #5)核算账簿管理
        # #点击核算账簿管理
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[4]/ul/li[5]/div/div/div/div[1]/span").click()
        # time.sleep(2)
        # #选择组织机构按钮
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/ul/li/span[1]/i").click()
        # #选择测试
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/ul/li/ul[7]/li/span[1]/i").click()
        # #选择00802测试02
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/ul/li/ul[7]/li/ul[2]/li/span[2]").click()
        # #点击关联账簿
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div[1]/button/span").click()
        # #关联账簿
        # #①单位选择
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[7]/div/span[1]").click()
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[7]/div[2]/div[2]/div/label/span").click()
        # #下一步
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[3]/div/button[2]").click()
        # #②账簿关联
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/fieldset/form/div[1]/div/div/div[1]/div/i").click()
        # #选择账簿
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/fieldset/form/div[1]/div/div/div[2]/ul[2]/li[1]").click()
        # #启用期间
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/fieldset/form/div[2]/div/div[1]/div[1]/div/span").click()
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/fieldset/form/div[2]/div/div[1]/div[2]/ul[2]/li[1]").click()
        # #启动期数
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/fieldset/form/div[2]/div/div[2]/div[1]/div/span").click()
        # #选择第2期
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/fieldset/form/div[2]/div/div[2]/div[2]/ul[2]/li[2]").click()
        # #点击下一步
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[3]/div/button[4]/span").click()
        # #③账簿检测，点击启用
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[3]/div/button[3]").click()
        # time.sleep(1)
        # #④完成启用，点击关闭
        # self.driver.find_element_by_xpath("/html/body/div[86]/div[2]/div/div/div[3]/div/button[3]").click()
        # time.sleep(1)


        # #切换目标用户进行基础数据的设置
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div/div/span").click()
        # #点击注销
        # self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[4]").click()
        # #登录
        # self.driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div/div[3]/div/form/div[1]/div/div[1]/input").send_keys("ceshi02")
        # self.driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div/div[3]/div/form/div[2]/div/div/input").send_keys("000000")
        # self.driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div/div[3]/div/form/div[3]/div/button").click()
        # self.driver.implicitly_wait(3)
        #
        # #基础数据
        # #点击基础数据
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/div").click()
        # #一、选择科目管理模块
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/ul/li[4]").click()
        # #选择会计科目，资产类
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[5]").click()
        # #点击新增
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/ul/li[1]/span/button").click()
        # #新增科目
        # #代码
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div[1]/div/div[1]/input").send_keys("19001")
        # #名称
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div[2]/div/div/input").send_keys("ceshi现金")
        # #助记码
        # #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div[3]/div/div/input").send_keys("10001")
        # #科目属性
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/span").click()
        # #选择普通科目
        # self.driver.find_element_by_xpath("/html/body/div[84]/ul[2]/li[1]").click()
        # #点击启用往来
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div[4]/div/label[2]/span[1]/input").click()
        # #明细核算要素，启用辅助项的往来单位
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/form/div[2]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[1]/div/label/span/input").click()
        # #点击保存
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/div/div[4]/div[2]/div/div/div[2]/div/button[3]/span").click()
        #
        # #二、基础数据_云核算
        # #点击基础数据_云核算模块
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/ul/li[3]/div/div/div/div[1]/span").click()
        # #创建定义
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[4]/div[1]/button/span").click()
        # #输入标识
        # self.driver.find_element_by_xpath("/html/body/div[99]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input").send_keys("ceshiooo")
        # #输入名称
        # self.driver.find_element_by_xpath("/html/body/div[99]/div[2]/div/div/div[2]/form/div[2]/div/div/input").send_keys("测试111")
        # #点击确定
        # self.driver.find_element_by_xpath("/html/body/div[99]/div[2]/div/div/div[3]/div/button[2]/span").click()
        #
        #
        #
        # #三、项目
        # #点击项目
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/ul/li[1]").click()
        # #点击新增
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[1]/button/span").click()
        # #项目信息，代码
        # self.driver.find_element_by_xpath("/html/body/div[160]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input").send_keys("10021")
        # #名称
        # self.driver.find_element_by_xpath("/html/body/div[160]/div[2]/div/div/div[2]/form/div[2]/div/div[1]/input").send_keys("cehsi项目")
        # #点击确定
        # self.driver.find_element_by_xpath("/html/body/div[160]/div[2]/div/div/div[3]/div/button[2]/span").click()
        #
        #
        # #四、往来单位
        # #点击往来单位
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/ul/li[5]/ul/li[2]/div/div/div/div[1]/span").click()
        # #点击新增
        # self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[1]/button/span").click()
        # #往来单位信息,代码
        # self.driver.find_element_by_xpath("/html/body/div[147]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input").send_keys("1001")
        # #名称
        # self.driver.find_element_by_xpath("/html/body/div[147]/div[2]/div/div/div[2]/form/div[2]/div/div/div[1]/input").send_keys("ceshi项目")
        # #点击确定
        # self.driver.find_element_by_xpath("/html/body/div[147]/div[2]/div/div/div[3]/div/button[2]/span").click()










if __name__ == '__main__':

    a = keYan_Ceshi
    # 读取yaml文件
    a.readYaml(a)
    #1.打开浏览器
    a.openBrower(a)
    #2.登录
    #a.signIn(a)
    #3.系统管理操作
    #a.sysManageOperate(a)
    #关闭浏览器
    #a.closeBrower(a)


