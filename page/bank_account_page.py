from base.base_action import BaseAction
from base.base_element import BaseElements
from base.base_logs import Logger
from page import logger


class BankAccountPage(BaseAction, BaseElements):

    def click_add_ac(self):
        # logger.info("点击Add Bank Account")
        self.click(self.Add_Bank_AC)

    def input_bank_cardno(self, cardno):
        # logger.info("输入银行账号或卡号")
        self.input(self.Edit_Bank_Card_No, cardno)

    def input_amount(self,amount):
        # logger.info("输入金额")
        self.input(self.enter_amount,amount)
    def click_confirm(self):
        # logger.info("点击确定按钮")
        self.click(self.Confirm_button)

    def click_back(self):
        # logger.info("点击返回")
        self.click(self.Back_button1)
