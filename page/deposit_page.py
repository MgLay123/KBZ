from base.base_action import BaseAction
from base.base_element import BaseElements


class DepositPage(BaseAction, BaseElements):

    def click_cashin_from_agent(self):
        self.click(self.Cashin_from_agent)

    def click_transfer_from_bankAC(self):
        self.click(self.Transfer_from_bankAC)

    def click_back(self):
        self.click(self.Back_button1)
