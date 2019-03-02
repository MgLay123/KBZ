from base.base_action import BaseAction
from base.base_element import BaseElements


class ReceivePage(BaseAction, BaseElements):

    def click_set_amount(self):
        self.click(self.Set_Amount)

    def click_save_image(self):
        self.click(self.Save_image)

    def input_amount(self, amount):
        self.input(self.Edit_amount, amount)

    def input_note(self, note):
        self.input(self.Add_note, note)

    def click_confirm(self):
        self.click(self.Confirm_button1)

    def click_back(self):
        self.click(self.Back_button1)
