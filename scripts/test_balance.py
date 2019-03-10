import time

import allure
import pytest
from base.analysis_data import AnalysisData
from base.base_assert import BaseAssert
from base.base_driver import init_driver
from base.base_element import BaseElements
from base.base_login import login
from page.page import Page
from base.base_data import *


class TestBalance(BaseElements,BaseAssert):

    def setup(self):
        self.page, self.driver = login()

    @allure.MASTER_HELPER.feature("通过Banlance界面CashIn")
    def test_diposit_agent(self):

        self.page.banner_page.click_balance()

        self.page.balance_page.click_deposit()

        self.page.deposit_page.click_cashin_from_agent()

        self.page.cash_in_page.click_start()

    @allure.MASTER_HELPER.feature("通过Banlance界面从银行卡向钱包转账")
    def test_diposit_bank_AC(self):

        self.page.banner_page.click_balance()

        self.page.balance_page.click_deposit()

        self.page.deposit_page.click_transfer_from_bankAC()

        self.page.bank_account_page.input_amount(amount)

        self.page.bank_account_page.click_confirm()

        self.page.pin_enter_page.input_pin()

        self.Assert_display(self.driver,self.assert_pay)

    @pytest.mark.parametrize("test_id,short_code", AnalysisData("balance_data").analysis_data())
    @allure.MASTER_HELPER.feature("通过Banlance界面向Agent做CashOut")
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
            self.Assert_display(self.driver, self.assert_pay)
        else:

            self.page.cash_out_page.input_amout(amount)
            self.page.cash_out_page.click_submit()
            self.page.pin_enter_page.input_pin()
            self.Assert_display(self.driver, self.assert_pay)

    @allure.MASTER_HELPER.feature("通过Banlance界面从ATM取钱")
    def test_withdraw_ATM(self):
        self.page.banner_page.click_balance()
        self.page.balance_page.click_withdraw()
        self.page.withdraw_page.click_cashout_from_ATM()
        self.page.cash_out_ATM_page.click_request_code()
        self.page.pin_enter_page.input_pin()
        self.Assert_display(self.driver, self.assert_ATM)

    @allure.MASTER_HELPER.feature("通过Banlance界面从钱包向银行卡转账")
    def test_withdraw_bank_AC(self):
        self.page.banner_page.click_balance()
        self.page.balance_page.click_withdraw()
        self.page.withdraw_page.click_transfer_from_bank_AC()
        self.page.bank_account_page.input_amount(amount)
        self.page.bank_account_page.click_confirm()
        self.page.pin_enter_page.input_pin()
        self.Assert_display(self.driver, self.assert_pay)

    def teardown(self):

        self.driver.quit()
