#coding=utf-8
_author_ = "K-DragonZ"
import unittest
import HTMLTestRunner

#相对路径
testcase_path = ".\\testcase"
report_path = ".\\report\\appium_report.html"
def creat_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test_*.py")
    for test_suite in discover:
        # print(test_suite)
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit

suite = creat_suite()
fp = open(report_path,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试结果",description="每平米商户版")
runner.run(suite)
fp.close()
