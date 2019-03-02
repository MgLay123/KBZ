from base.base_action import BaseAction
from base.base_element import BaseElements


class PinManagePage(BaseAction,BaseElements):

    def click_change_pin(self):
        self.click(self.Change_pin_button)

    def click_forget_pin(self):
        self.click(self.Forget_pin_button)

    def click_back(self):
        self.click(self.Back_button1)