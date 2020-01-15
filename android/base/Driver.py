import os
from appium import webdriver


class Driver(object):

    # 防止多个用例执行时-重启app
    @staticmethod
    def getInstance():
        if (hasattr(Driver, 'instance')): #返回单一实例
            return Driver.instance

        # os.system('adb uninstall io.appium.settings')
        # os.system('adb uninstall io.appium.unlock')

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'samsung'
        desired_caps['app'] = r'D:\proj\testDP\app\build\outputs\apk\debug\app-debug.apk'
        desired_caps['appPackage'] = 'cn.ycf.testdp'
        desired_caps['appActivity'] = 'cn.ycf.testdp.TestDPActivity'
        desired_caps['noReset'] = True # 不清除数据，不会重新安装
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        driver.quit = lambda : {} #不关闭app
        Driver.instance = driver
        return driver
