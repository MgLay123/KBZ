import time

from base.base_action import BaseAction
from base.base_element import BaseElements


class PinEnterPage(BaseAction, BaseElements):

    def click_cancel(self):
        self.click(self.PIN_Cancel)

    def click_forget_pin(self):
        self.click(self.Forget_pin)

    def input_pin(self):
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
        self.click(self.Delete_PIN)