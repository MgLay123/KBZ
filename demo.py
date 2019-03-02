#
# from telnetlib import EC
#
# import time
# from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# from base.base_action import BaseAction
# from base.base_element import BaseElements
#
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '5.1'
# desired_caps['deviceName'] = '192.168.56.101:5555'
# desired_caps['appPackage'] = 'com.kbzbank.kpaycustomer.ceshi'
# desired_caps['appActivity'] = 'com.chinasoft.kbz.ui.login.LoginActivity'
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
# driver.find_element(By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edt_phone_number").send_keys("770013073")
# time.sleep(3)
# driver.find_element(By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edt_verification_code").send_keys("666888")
# time.sleep(3)
# driver.find_element(By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_start").click()
#
# while True:
#     try:
#
#         driver.find_element(By.XPATH, "//*[@text = 'Aeon']")
#
#     except:
#         TouchAction(driver).press(x=650, y=1300).move_to(x=650, y=100).release().perform()

str = "100"
for i  in str:
    print(i.isalpha())

print(ord('-'))