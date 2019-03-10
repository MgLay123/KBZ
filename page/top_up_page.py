from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class TopUpPage(BaseAction, BaseElements):

    def input_phone_no(self, phoneno):
       # logger.info("输入 手机号")
        self.input(self.Edit_Phone_no, phoneno)

    def click_MMK(self):
       # logger.info("选择2000MMK")
        self.click(self.MMK2000)

    def click_topup_history(self):
       # logger.info("点击 充值历史")
        self.click(self.Topup_history)

    def click_contact(self):
       # logger.info("点击 联系")
        self.click(self.contact)

    def click_back(self):
       # logger.info("点击 返回")
        self.click(self.Back_button1)
