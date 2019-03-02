from base.base_action import BaseAction
from base.base_element import BaseElements


class ChangePinPage(BaseAction, BaseElements):

    def input_old_pin(self, old_pin):
        self.input(self.Old_pin_input, old_pin)

    def input_new_pin(self, new_pin):
        self.input(self.New_pin_input, new_pin)

    def input_confirm_pin(self, new_pin):
        self.input(self.Confirm_pin_input, new_pin)

    def click_confirm(self):
        self.click(self.Confirm_button)

    def click_back(self):
        self.click(self.Back_button1)
