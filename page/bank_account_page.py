from base.base_action import BaseAction
from base.base_element import BaseElements


class BankAccountPage(BaseAction, BaseElements):

    def click_add_ac(self):
        self.click(self.Add_Bank_AC)

    def input_bank_cardno(self, cardno):
        self.input(self.Edit_Bank_Card_No, cardno)

    def input_amount(self,amount):
        self.input(self.enter_amount,amount)
    def click_confirm(self):
        self.click(self.Confirm_button)

    def click_back(self):
        self.click(self.Back_button1)
