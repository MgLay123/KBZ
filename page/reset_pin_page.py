from base.base_action import BaseAction
from base.base_element import BaseElements


class ResetPinPage(BaseAction, BaseElements):

    def input_kyc(self, kyc_no):
        self.input(self.Edit_KYC, kyc_no)

    def click_confirm(self):
        self.click(self.Confirm_button)

    def click_back(self):
        self.click(self.Back_button1)
