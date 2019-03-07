
from telnetlib import EC

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from base.base_action import BaseAction
from base.base_element import BaseElements

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.kbzbank.kpaycustomer.ceshi'
desired_caps['appActivity'] = 'com.chinasoft.kbz.ui.login.LoginActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

def if_display(text):
    for i in range(10):

        if text in  driver.page_source:
            print('可以执行下一步了')
            break
        else:
            time.sleep(2)
            print("aaaaaa")
            if i == 9:
                raise Exception("页面加载超时！")


if_display('Welcome')
driver.find_element(By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edt_phone_number").send_keys("770013073")
time.sleep(3)
driver.find_element(By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edt_verification_code").send_keys("666888")
time.sleep(3)
driver.find_element(By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_start").click()
if_display('KBZPay ceshi')



