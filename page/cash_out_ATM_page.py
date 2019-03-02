from base.base_action import BaseAction
from base.base_element import BaseElements


class CashoutATMPage(BaseAction, BaseElements):

    def click_no_longer_display(self):
        self.click(self.No_longer_display)

    def click_request_code(self):
        self.click(self.Request_code)

    def click_search_ATM(self):
        self.click(self.Search_ATM)

    def click_back(self):
        self.click(self.Back_button1)
