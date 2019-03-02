from base.base_action import BaseAction
from base.base_element import BaseElements


class WithDrawPage(BaseAction, BaseElements):

    def click_cashout_from_agent(self):
        self.click(self.CashOut_agent)

    def click_cashout_from_ATM(self):
        self.click(self.CashOut_from_ATM)

    def click_transfer_from_bankAC(self):
        self.click(self.CashOut_from_BankAC)

    def click_back(self):
        self.click(self.Back_button1)
