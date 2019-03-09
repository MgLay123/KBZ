import time
from base.base_data import *
import pytest
import allure

from base.analysis_data import AnalysisData
from base.base_driver import init_driver
from base.base_login import login
from page.page import Page


class TestScanAndPay:

    def setup(self):
        self.page, self.driver = login()

    @pytest.mark.parametrize("test_id,code", AnalysisData("scan_and_pay").analysis_data())
    @allure.MASTER_HELPER.feature("Manual Pay 测试用例")
    def test_manual_pay(self, test_id, code):
        self.page.banner_page.click_scanQR()
        self.page.scanqr_page.click_manual()
        self.page.manual_page.click_choose_type()


        if test_id == case_1:

            self.page.manual_page.click_choose_merchant()
            self.page.manual_page.input_code(code)
            self.page.manual_page.click_enter()
            self.page.payment_page.input_amount(amount)
            self.page.payment_page.click_notes()
            self.page.payment_page.input_notes(notes)
            self.page.payment_page.click_payemnt()



        elif test_id == case_2:
            self.page.manual_page.click_choose_agent()
            self.page.manual_page.input_code(code)
            self.page.manual_page.click_enter()
            self.page.cash_out_page.click_MMK()
            self.page.cash_out_page.click_submit()


        else:
            self.page.manual_page.click_choose_person()
            self.page.manual_page.input_code(code)
            self.page.manual_page.click_enter()
            self.page.payment_page.input_amount(amount)
            self.page.payment_page.click_notes()
            self.page.payment_page.input_notes(notes)
            self.page.transfer_page.click_transfer()


        self.page.pin_enter_page.input_pin()
        time.sleep(3)

    def teardown(self):
        self.driver.quit()
