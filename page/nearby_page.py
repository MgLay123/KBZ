from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class NearByPage(BaseAction, BaseElements):

    def input_Address(self, address):
        # logger.info("输入 Address")
        self.input(self.Edit_Address, address)

    def click_contact(self):
        # logger.info("点击 Contact")
        self.click(self.Get_phoneno_contact)

    def click_submit(self):
        # logger.info("点击 提交")
        self.click(self.Submit_button)

    def input_amount(self, amount):
        # logger.info("输入 金额")
        self.input(self.Edit_amount, amount)

    def input_notes(self, note):
        # logger.info("点击 Notes")
        self.input(self.Add_note, note)

    def click_transfer(self):
        # logger.info("点击 Transfer")
        self.click(self.Transfer)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)
