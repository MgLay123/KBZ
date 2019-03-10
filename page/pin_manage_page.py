from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class PinManagePage(BaseAction,BaseElements):

    def click_change_pin(self):
        # logger.info("点击 Change Pin")
        self.click(self.Change_pin_button)

    def click_forget_pin(self):
        # logger.info("点击 Forget PIN")
        self.click(self.Forget_pin_button)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)