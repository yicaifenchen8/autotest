import unittest
import selenium
import time
import os
from appium import webdriver
from android.base.Driver import Driver
from android.test_case.R import R


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.driver = Driver.getInstance()

    def test_click(self):
        print('test_click')
        time.sleep(1)

        # R.login

        # self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.TextView[contains(@text,'测试')]").click()
        # self.driver.find_element_by_id('cn.ycf.testdp:id/msg').click()

    def tearDown(self):
        self.driver.quit()
        print('tearDown')


if __name__ == '__main__':
    unittest.main()
