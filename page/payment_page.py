from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class PaymentPage(BaseAction, BaseElements):

    def input_amount(self, amount):
        # logger.info("输入 金额")
        self.input(self.Edit_amount, amount)

    def click_notes(self):
        # logger.info("点击 Notes")
        self.click(self.Add_note)

    def input_notes(self, note):
        # logger.info("输入 Notes")
        self.input(self.edit_notes, note)

    def click_payemnt(self):
        # logger.info("点击 支付")
        self.click(self.payment)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button)
