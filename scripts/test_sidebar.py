import time

import pytest
from appium.webdriver.common.touch_action import TouchAction

from base.analysis_data import AnalysisData
from base.base_driver import init_driver
from base.base_element import BaseElements
from base.base_login import login
from page.page import Page

from base.base_data import *


class TestSidebar(BaseElements):

    def setup(self):
        self.page, self.driver = login()
        self.page.banner_page.click_drawer()

    def test_set_photo(self):
        self.page.sidebar_page.click_photo()
        self.page.set_photo_page.click_choose_photo()
        time.sleep(5)
        TouchAction(self.driver).tap(x=500, y=500).release().perform()
        time.sleep(2)
        self.driver.find_element_by_xpath(save_xpath).click()

    def test_set_lang_my(self):
        self.page.sidebar_page.click_setting()
        self.page.setting_page.click_lang()
        self.page.language_page.click_my()

    def test_set_lang_ch(self):
        self.page.sidebar_page.click_setting()
        self.page.setting_page.click_lang()
        self.page.language_page.click_ch()

    def test_set_lang_en(self):
        self.page.sidebar_page.click_setting()
        self.page.setting_page.click_lang()
        self.page.language_page.click_en()

    def test_set_noti_sound(self):
        self.page.sidebar_page.click_setting()
        self.page.setting_page.click_notices()
        self.page.new_notices_page.click_sound()

    def test_set_noti_vibrate(self):
        self.page.sidebar_page.click_setting()
        self.page.setting_page.click_notices()
        self.page.new_notices_page.click_vibrade()

    def test_change_pin(self):
        self.page.sidebar_page.click_setting()
        self.page.setting_page.click_PIN_manage()
        self.page.pin_manage_page.click_change_pin()

    def test_forget_pin(self):
        self.page.sidebar_page.click_setting()
        self.page.setting_page.click_PIN_manage()
        self.page.pin_manage_page.click_forget_pin()

    def test_feed_back(self):
        self.page.sidebar_page.click_help()
        self.page.help_feeback_page.click_feeback()

    def test_logout(self):
        self.page.sidebar_page.click_logout()
        self.page.sidebar_page.click_cancel()
        self.page.sidebar_page.click_logout()
        self.page.sidebar_page.click_confirm()

    def teardown(self):
        time.sleep(2)
        self.driver.quit()
