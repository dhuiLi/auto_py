# -*- coding: utf-8 -*-
import os
import unittest
import time
from HTMLTestRunner import HTMLTestRunner


def _main():
    print('========== START ==========')
    testdir = os.path.dirname(os.path.dirname(__file__))  #获取项目的根目录
    test_dir = os.path.join(testdir, 'acct')  # 测试用例文件夹
    test_report = test_dir + '/report'
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    report_file_name = 'result_' + now + '.html'  #测试报告名字
    report_file_dir = test_report + '/' + report_file_name  #测试报告路径
    # 自动搜索项目根目录下的所有case,构造测试集;返回TestSuit对象
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='case_*.py')
    #报告详情
    fp = open(report_file_dir, 'wb')
    runner = HTMLTestRunner(stream=fp, title="测试报告", description='用例执行情况：')
    runner.run(discover)

#邮件
    # fp.close()
    # email = Email()
    # # 执行发送邮件
    # new_report = email.new_report(test_report)
    # email.send_mail(new_report)
    print('========== END ==========')


if __name__ == "__main__":
    _main()
