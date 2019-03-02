from base.base_action import BaseAction
from base.base_element import BaseElements


class TopUpPage(BaseAction, BaseElements):

    def input_phone_no(self, phoneno):
        self.input(self.Edit_Phone_no, phoneno)

    def click_MMK(self):
        self.click(self.MMK2000)

    def click_topup_history(self):
        self.click(self.Topup_history)

    def click_contact(self):
        self.click(self.contact)

    def click_back(self):
        self.click(self.Back_button1)
