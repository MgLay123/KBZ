from appium.webdriver.common.touch_action import TouchAction

from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class QuickPayPage( BaseAction,BaseElements):

    def click_Aeon(self):
        # logger.info("点击 Aeon")
        self.click(self.Select_Aeon)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)

    def click_quick_pay(self):
        # logger.info("点击 Quick Pay")
        self.move_and_click(self.QuickPay_button)

    def click_mother_finance(self):
        # logger.info("点击 Mother Finance")
        self.move_and_click(self.mother_finance)

    def input_customer_id(self, id):
        # logger.info("输入 Customer ID")
        self.click_and_input(700, 1170, id)

    def input_name(self, name):
        # logger.info("输入 Name")
        self.click_and_input(700, 1500, name)

    def input_nrc(self, nrc):
        # logger.info("输入 NRC")
        self.click_and_input(700, 1840, nrc)

    def input_mobile_num(self, mobile_num):
        # logger.info("输入 手机号码")
        self.click_and_input(700, 2150, mobile_num)

    def input_amount(self, amount):
        # logger.info("输入 金额")
        self.move_and_input(self.Other_amount, amount)

    def click_submit(self):
        # logger.info("点击 提交")
        self.move_and_click(self.Submit_button)

    def input_aeon_ref_num(self, ref_num):
        # logger.info("输入 Reference Num")
        self.click_and_input(600, 1170, ref_num)

    def input_aeon_depoistor_name(self, depoistor_name):
        # logger.info("输入 DeSpoistor Name")
        self.click_and_input(700, 1500, depoistor_name)

    def input_aeon_test(self, test):
        # logger.info("输入 test")
        self.click_and_input(700, 2150, test)

    def click_confirm(self):
        # logger.info("点击 确定")
        self.click(self.Confirm_button)
