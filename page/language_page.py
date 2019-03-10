from base.base_action import BaseAction
from base.base_element import BaseElements
from base.base_logs import Logger
from page import logger


class LanguagePage(BaseAction,BaseElements):

    def click_en(self):
        # logger.info("选择英文语言")
        self.click(self.lang_en)

    def click_ch(self):
        # logger.info("选择中文语言")
        self.click(self.lang_ch)

    def click_my(self):
        # logger.info("选择缅文语言")

        self.click(self.lang_my)

    def click_back(self):
        # logger.info("点击 返回")

        self.click(self.Back_button1)