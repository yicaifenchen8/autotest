import unittest
import os
from selenium import webdriver
from time import sleep
# import HTMLTestRunner
import time

class Dttest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start setup')
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['deviceName'] = 'iPhone 5s'

        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('tearDown')

    def test_slideAndPressSure(self):
        sleep(10)
        print('test passed')

    def test_click(self):
        self.driver.find_element_by_name('point:').click()
        sleep(5)
        print('click passed')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Dttest('test_slideAndPressSure'))
    suite.addTest(Dttest('test_click'))
    unittest.TextTestRunner(verbosity=2).run(suite)

    # timestr = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
    # filename = '/Users/lihui/Documents/PycharmProjects/test/report/'+timestr+'.html'
    # fp = open(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title='result',
    #     description='report'
    # )
    # runner.run(suite)
    # fp.close()