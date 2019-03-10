from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class ResetPinPage(BaseAction, BaseElements):

    def input_kyc(self, kyc_no):
        # logger.info("输入 KYC信息")
        self.input(self.Edit_KYC, kyc_no)

    def click_confirm(self):
        # logger.info("点击 确定")
        self.click(self.Confirm_button)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)
