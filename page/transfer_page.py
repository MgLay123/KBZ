from base.base_action import BaseAction
from base.base_element import BaseElements


class TransferPage(BaseAction, BaseElements):

    def input_phone_no(self, phoneno):
        self.input(self.Edit_Phone_no, phoneno)

    def click_search(self):
        self.click(self.Search_button)

    def click_back(self):
        self.click(self.Back_button1)



    def click_confirm_yes(self):
        self.click(self.confirm_yes)

    def click_transfer(self):
        self.click(self.Transfer)

    def  input_amount(self,amount):

        self.input(self.Edit_amount,amount)

    def click_submit(self):
        self.click(self.Submit_button)

    def click_start(self):
        self.click(self.Confirm_button)
