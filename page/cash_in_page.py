from base.base_action import BaseAction
from base.base_element import BaseElements


class CashinPage(BaseAction, BaseElements):

    def click_agent(self):
        self.click(self.Agent)

    def click_bank_ac(self):
        self.click(self.Bank_account)

    def click_no_longer_display(self):
        self.click(self.No_longer_display)

    def click_start(self):
        self.click(self.Confirm_button)

    def click_back(self):
        self.click(self.Back_button1)
