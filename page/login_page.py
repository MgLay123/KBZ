import logging

from base.base_action import BaseAction
from base.base_element import BaseElements
# from base.base_logs import Logger
from page import logger


class LoginPage(BaseAction, BaseElements):

    def click_lang_button(self):
        # logger.info("点击 语言")
        self.click(self.lang_button)

    def click_en_button(self):
        # logger.info('选择英文语言')
        self.click(self.lang_en)

    def click_my_button(self):
        # logger.info("选择缅文语言")
        self.click(self.lang_my)

    def click_ch_button(self):
        # logger.info("选择中文语言")
        self.click(self.lang_ch)

    def click_sidebar(self):
        # logger.info("点击 侧边栏")
        self.click(self.sidebar_button)

    def click_sidebar_nearby(self):
        # logger.info("点击 侧边栏NearBy")
        self.click(self.sidebar_nearby)

    def click_sidebar_feeback(self):
        # logger.info("点击 侧边栏FeedBack")
        self.click(self.sidebar_feeback)

    def click_sidebar_about(self):
        # logger.info("点击 侧边栏关于")
        self.click(self.sidebar_about)

    def input_phoneNO(self, phoneNO):
        # logger.info("输入 手机号码")
        self.input(self.phoneNO_input, phoneNO)

    def input_smscode(self, smscode):
        # logger.info("输入 短信验证码")
        self.input(self.sms_input, smscode)

    def click_getcode(self):
        # logger.info("点击 获取验证码")
        self.click(self.getcode_button)

    def click_start(self):
        # logger.info("点击 Start")
        self.click(self.start_button)

    def find_start(self):

        return self.find_element(self.start_button).text

    def start_status(self):
        return self.find_element(self.start_button_status)

    def find_title(self):
        return self.find_element(self.title)

    def find_start_status(self, name):
        return self.find_element(self.start_button).get_attribute(name)

    def find_code_status(self, name):
        return self.find_element(self.getcode_button).get_attribute(name)

    def click_term(self):
        # logger.info("点击 Term")
        self.click(self.agreement_select)
