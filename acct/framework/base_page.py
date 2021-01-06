import os

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException




class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def _open(self, url, page_title=None):
        """
        打开指定网页
        :param page_title: 网页title, 非必填
        :return: 若传入的page_title与网页title不同则触发断言
        """
        self.driver.get(url=url)


    # 重写元素定位方法
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element_by_xpath(*loc).is_displayed())
            return self.driver.find_element_by_xpath(*loc)
        except(NoSuchElementException, TimeoutException):
            # self._driver.quit()
            # logger.error('[{}]寻找元素失败, 定位方式为xpath:{}'.format(os.path.basename(__file__), loc))
            raise TimeoutException(msg='[{}]寻找元素失败, 定位方式为xpath:{}'.format(os.path.basename(__file__), loc))

    def takeScreenshot(self,imgName):
        '''截图函数'''
        test_d = os.path.dirname(os.path.dirname(__file__))  #获取当前根目录
        now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
        img_time = now + '.png'
        test_screen = test_d + '/screenshots'  #截图保存路径
        self.driver.get_screenshot_as_file('{}/{}_{}'.format(os.path.abspath(test_screen), imgName,img_time))

        # 重写定义send_keys方法
    def send_keys(self, el, vaule, clear_first=True, click_first=True):
        try:
            if click_first:
                el.click()
            if clear_first:
                el.clear()
                el.send_keys(vaule)
        except (NoSuchElementException, TimeoutException) as e:
            # NoSuchElementException:
            # logger.error("[{}]页面中未能找到元素{}".format(os.path.basename(__file__), e))
            raise NoSuchElementException(msg='[{}]页面中未能找到元素{}'.format(os.path.basename(__file__), e))

