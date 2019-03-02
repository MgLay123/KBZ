from base.base_action import BaseAction
from base.base_element import BaseElements


class BalancePage(BaseAction, BaseElements):

    def click_withdraw(self):
        self.click(self.withdraw_button)

    def click_deposit(self):
        self.click(self.deposit_button)

    def click_history(self):
        self.click(self.History_button)

    def click_back(self):
        self.click(self.Back_button1)
