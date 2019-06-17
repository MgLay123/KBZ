from appium import webdriver
import os

def init_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['appPackage'] = 'com.kbzbank.kpaycustomer.ceshi'
    desired_caps['appActivity'] = 'com.chinasoft.kbz.ui.base.LaunchActivity'
    PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
    desired_caps['app'] = PATH('C:\\Users\\29405\\Desktop\\KBZ\\KBZPay_2.0.0_ceshi.apk')
    desired_caps['automationName'] = 'Uiautomator2'

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

