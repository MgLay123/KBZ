from base.base_action import BaseAction
from base.base_element import BaseElements


class PaymentPage(BaseAction, BaseElements):

    def input_amount(self, amount):
        self.input(self.Edit_amount, amount)

    def click_notes(self):
        self.click(self.Add_note)

    def input_notes(self, note):
        self.input(self.edit_notes, note)

    def click_payemnt(self):
        self.click(self.payment)

    def click_back(self):
        self.click(self.Back_button)
