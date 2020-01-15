import unittest
import os
from selenium import webdriver
from time import sleep
from android.base.Driver import Driver


class Dttest(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.driver = Driver.getInstance()

    def test_slideAndPressSure(self):
        print('test_slideAndPressSure')
        sleep(1)

    def test_click(self):
        print('test_click')
        sleep(1)

    def tearDown(self):
        self.driver.quit()
        print('tearDown')


if __name__ == '__main__':
    unittest.main()
