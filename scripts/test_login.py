import time

import allure

from base.base_data import *
import pytest

from base.analysis_data import AnalysisData
from base.base_driver import init_driver
from base.base_logs import Logger
from page.page import Page


class TestLogin:

    def setup(self):

        self.driver = init_driver()
        self.page = Page(self.driver)
        self.page.login_page.click_get_start()
        self.page.login_page.click_update_cancel()

    @allure.MASTER_HELPER.feature("Login UI set language")
    def test_change_lang(self):

        self.page.login_page.click_lang_button()

        self.page.login_page.click_en_button()

        assert self.page.login_page.find_start() == login_lang_en

        self.page.login_page.click_lang_button()

        self.page.login_page.click_my_button()

        assert self.page.login_page.find_start() == login_lang_my

        self.page.login_page.click_lang_button()

        self.page.login_page.click_ch_button()

        assert self.page.login_page.find_start() == login_lang_ch

    # 使用pytest实现多用例执行
    @pytest.mark.parametrize("test_id,phoneNo,smscode", AnalysisData("login_data").analysis_data())
    @allure.MASTER_HELPER.feature("Login")
    def test_login(self, test_id, phoneNo, smscode):

        self.page.login_page.input_phoneNO(phoneNo)
        self.page.login_page.input_smscode(smscode)
        self.page.login_page.click_start()
        if test_id == case_1:
            assert self.page.login_page.find_toast(login_toast_no)

        elif test_id == case_2:
            time.sleep(2)
            assert self.page.login_page.find_title()

        elif test_id == case_3:
            assert self.page.login_page.find_toast(login_toast_wrong)

        elif test_id == case_4:
            time.sleep(2)
            assert self.page.login_page.find_start_status(login_status) == login_toast_false

        else:
            assert self.page.login_page.find_toast(login_toast_mobile)

    @allure.MASTER_HELPER.feature("Login By Term")
    def test_login_by_term(self):

        self.page.login_page.input_phoneNO(phoneNo)
        assert self.page.login_page.find_code_status(login_status) == login_toast_true
        self.page.login_page.input_smscode(smscode)
        assert self.page.login_page.find_start_status(login_status) == login_toast_true
        self.page.login_page.click_term()
        assert self.page.login_page.find_start_status(login_status) == login_toast_false
        assert self.page.login_page.find_code_status(login_status) == login_toast_false

    def teardown(self):
        self.driver.quit()
