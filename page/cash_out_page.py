from base.base_action import BaseAction
from base.base_element import BaseElements


class CashoutPage(BaseAction, BaseElements):

    def click_no_longer_display(self):
        self.click(self.No_longer_display)

    def click_at_agent(self):
        self.click(self.At_agent)

    def input_agent_short_code(self, short_code):
        self.input(self.Edit_agent, short_code)

    def click_scan_agent(self):
        self.click(self.Scan_agent)

    def click_next(self):
        self.click(self.Next_button)

    def click_MMK(self):
        self.click(self.MMK800)

    def input_amout(self, amount):
        self.input(self.Other_amount, amount)

    def click_cashout_all(self):
        self.click(self.Cashout_all)

    def click_submit(self):
        self.click(self.Submit_button)

    def click_locate_agent(self):
        self.click(self.Find_agent_map)

    def click_back(self):
        self.click(self.Back_button1)
