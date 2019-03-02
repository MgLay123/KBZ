from base.base_action import BaseAction
from base.base_element import BaseElements


class ForgetPinPage(BaseAction, BaseElements):

    def click_reset_now(self):
        self.click(self.Reset_now_button)

    def click_back(self):
        self.click(self.Back_button1)
