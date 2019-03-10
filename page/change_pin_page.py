from base.base_action import BaseAction
from base.base_element import BaseElements
from base.base_logs import Logger
from page import logger


class ChangePinPage(BaseAction, BaseElements):

    def input_old_pin(self, old_pin):
        # logger.info("输入 Old PIN")
        self.input(self.Old_pin_input, old_pin)

    def input_new_pin(self, new_pin):
        # logger.info("输入 New PIN")
        self.input(self.New_pin_input, new_pin)

    def input_confirm_pin(self, new_pin):
        # logger.info("再次输入 New PIN")
        self.input(self.Confirm_pin_input, new_pin)

    def click_confirm(self):
        # logger.info("点击 确定")
        self.click(self.Confirm_button)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)
