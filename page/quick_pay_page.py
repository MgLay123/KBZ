from appium.webdriver.common.touch_action import TouchAction

from base.base_action import BaseAction
from base.base_element import BaseElements


class QuickPayPage(BaseAction, BaseElements):

    def click_Aeon(self):
        self.click(self.Select_Aeon)

    def click_back(self):
        self.click(self.Back_button1)

    def click_quick_pay(self):
        self.move_and_click(self.QuickPay_button)

    def click_mother_finance(self):
        self.move_and_click(self.mother_finance)

    def input_customer_id(self, id):
        self.click_and_input(700, 1170, id)

    def input_name(self, name):
        self.click_and_input(700, 1500, name)

    def input_nrc(self, nrc):
        self.click_and_input(700, 1840, nrc)

    def input_mobile_num(self, mobile_num):
        self.click_and_input(700, 2150, mobile_num)

    def input_amount(self, amount):
        self.move_and_input(self.Other_amount, amount)

    def click_submit(self):
        self.move_and_click(self.Submit_button)

    def input_aeon_ref_num(self, ref_num):
        self.click_and_input(600, 1170, ref_num)

    def input_aeon_depoistor_name(self, depoistor_name):
        self.click_and_input(700, 1500, depoistor_name)

    def input_aeon_test(self, test):
        self.click_and_input(700, 2150, test)

    def click_confirm(self):
        self.click(self.Confirm_button)
