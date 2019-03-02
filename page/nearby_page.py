from base.base_action import BaseAction
from base.base_element import BaseElements


class NearByPage(BaseAction, BaseElements):

    def input_Address(self, address):
        self.input(self.Edit_Address, address)

    def click_contact(self):
        self.click(self.Get_phoneno_contact)

    def click_submit(self):
        self.click(self.Submit_button)

    def input_amount(self, amount):
        self.input(self.Edit_amount, amount)

    def input_notes(self, note):
        self.input(self.Add_note, note)

    def click_transfer(self):
        self.click(self.Transfer)

    def click_back(self):
        self.click(self.Back_button1)
