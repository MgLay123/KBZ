import time
import pytest
from base.analysis_data import AnalysisData
from base.base_driver import init_driver
from base.base_element import BaseElements
from base.base_login import login
from page.page import Page
from base.base_data import *


class TestNotify(BaseElements):

    def setup(self):
        self.page, self.driver = login()

    def test_diposit_agent(self):
        self.page.banner_page.click_balance()
        self.page.balance_page.click_deposit()
        self.page.deposit_page.click_cashin_from_agent()
        self.page.cash_in_page.click_start()

    def test_diposit_bank_AC(self):
        self.page.banner_page.click_balance()
        self.page.balance_page.click_deposit()
        self.page.deposit_page.click_transfer_from_bankAC()
        self.page.bank_account_page.input_amount(amount)
        self.page.bank_account_page.click_confirm()
        self.page.pin_enter_page.input_pin()

    @pytest.mark.parametrize("test_id,short_code", AnalysisData("balance_data").analysis_data())
    def test_withdraw_agent(self,test_id, short_code):
        self.page.banner_page.click_balance()
        self.page.balance_page.click_withdraw()
        self.page.withdraw_page.click_cashout_from_agent()
        self.page.cash_out_page.click_at_agent()
        self.page.cash_out_page.input_agent_short_code(short_code)
        self.page.cash_out_page.click_next()
        if test_id == case_1:

            self.page.cash_out_page.click_MMK()
            self.page.cash_out_page.click_submit()
            self.page.pin_enter_page.input_pin()
        else:

            self.page.cash_out_page.input_amout(amount)
            self.page.cash_out_page.click_submit()
            self.page.pin_enter_page.input_pin()
            time.sleep(2)

    def test_withdraw_ATM(self):
        self.page.banner_page.click_balance()
        self.page.balance_page.click_withdraw()
        self.page.withdraw_page.click_cashout_from_ATM()
        self.page.cash_out_ATM_page.click_request_code()
        self.page.pin_enter_page.input_pin()

    def test_withdraw_bank_AC(self):
        self.page.banner_page.click_balance()
        self.page.balance_page.click_withdraw()
        self.page.withdraw_page.click_transfer_from_bankAC()
        self.page.bank_account_page.input_amount(amount)
        self.page.bank_account_page.click_confirm()
        self.page.pin_enter_page.input_pin()

    def teardown(self):

        self.driver.quit()
