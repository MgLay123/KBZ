import time
import pytest
from base.analysis_data import AnalysisData
from base.base_driver import init_driver
from base.base_element import BaseElements
from base.base_login import login
from page.page import Page
from base.base_data import *


class TestTransfer(BaseElements):

    def setup(self):
        self.page, self.driver = login()

    @pytest.mark.parametrize("test_id,phone_no", AnalysisData("transfer_data").analysis_data())
    def test_transfer(self,test_id, phone_no):
        self.page.banner_page.click_Tansfer()
        self.page.transfer_page.input_phone_no(phone_no)
        self.page.transfer_page.click_submit()

        if test_id == case_1:
            self.page.transfer_page.click_confirm_yes()
            self.page.transfer_page.click_start()
            self.page.transfer_page.input_amount(amount)
            self.page.transfer_page.click_transfer()
            self.page.pin_enter_page.input_pin()
        else:

            self.page.transfer_page.input_amount(amount)
            self.page.transfer_page.click_transfer()
            self.page.pin_enter_page.input_pin()
            time.sleep(2)



    def teardown(self):

        self.driver.quit()
