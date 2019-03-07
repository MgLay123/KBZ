import time
import pytest
from appium.webdriver.common.touch_action import TouchAction

from base.analysis_data import AnalysisData
from base.base_assert import BaseAssert
from base.base_driver import init_driver
from base.base_element import BaseElements
from base.base_login import login


from page.page import Page
from base.base_data import *


class TestQuickPay(BaseElements,BaseAssert):

    def setup(self):
        self.page, self.driver = login()


    # def test_mother_finance(self):
    #     self.page.quick_pay_page.click_quick_pay()
    #     self.page.quick_pay_page.click_mother_finance()
    #     self.page.quick_pay_page.input_customer_id(customer_id)
    #     self.page.quick_pay_page.input_name(name)
    #     self.page.quick_pay_page.input_nrc(nrc)
    #     self.page.quick_pay_page.input_mobile_num(mobile_num)
    #     self.page.quick_pay_page.input_amount(amount)
    #     self.page.quick_pay_page.click_submit()
    #     self.page.pin_enter_page.input_pin()

    def test_aeon(self):
        quick_pay_page = self.page.quick_pay_page
        quick_pay_page.click_quick_pay()
        quick_pay_page.click_Aeon()
        self.if_display(self.driver,self.ref)
        quick_pay_page.input_aeon_ref_num(ref_num)
        quick_pay_page.input_aeon_depoistor_name(depoistor_name)
        quick_pay_page.input_aeon_test(test)
        quick_pay_page.input_amount(amount)
        quick_pay_page.click_submit()
        quick_pay_page.click_confirm()
        self.page.pin_enter_page.input_pin()

    def teardown(self):
        time.sleep(1)
        self.driver.quit()
