from base.base_action import BaseAction
from base.base_element import BaseElements
from base.base_logs import Logger
from page import logger


class ForgetPinPage(BaseAction, BaseElements):

    def click_reset_now(self):
        # logger.info("点击 Reset Now")
        self.click(self.Reset_now_button)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)
