import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import init_driver
from base.base_logs import Logger
from page.page import Page
from base.base_data import *


# 初始化登录
def login():
    driver = init_driver()
    page = Page(driver)
    page.login_page.click_get_start()
    page.login_page.click_update_cancel()
    page.login_page.input_phoneNO(phoneNo)
    page.login_page.input_smscode(smscode)

    page.login_page.click_start()
    return page, driver
