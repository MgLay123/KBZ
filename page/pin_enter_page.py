import time

from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class PinEnterPage(BaseAction, BaseElements):

    def click_cancel(self):
        # logger.info("点击 取消")
        self.click(self.PIN_Cancel)

    def click_forget_pin(self):
        # logger.info("点击 忘记密码")
        self.click(self.Forget_pin)

    def input_pin(self):
        # logger.info("输入密码")
        self.click(self.PIN_1)
        time.sleep(1)
        self.click(self.PIN_4)
        time.sleep(1)
        self.click(self.PIN_7)
        time.sleep(1)
        self.click(self.PIN_2)
        time.sleep(1)
        self.click(self.PIN_5)
        time.sleep(1)
        self.click(self.PIN_8)

    def click_delete(self):
        # logger.info("点击 删除")
        self.click(self.Delete_PIN)