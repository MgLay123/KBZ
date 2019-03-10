from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class TransferPage(BaseAction, BaseElements):

    def input_phone_no(self, phoneno):
       # logger.info("输入 手机号码")
        self.input(self.Edit_Phone_no, phoneno)

    def click_search(self):
       # logger.info("点击 搜索")
        self.click(self.Search_button)

    def click_back(self):
       # logger.info("点击 返回")
        self.click(self.Back_button1)



    def click_confirm_yes(self):
       # logger.info("点击 YES")
        self.click(self.confirm_yes)

    def click_transfer(self):
       # logger.info("点击 Transfer")
        self.click(self.Transfer)

    def  input_amount(self,amount):
       # logger.info("输入 金额")

        self.input(self.Edit_amount,amount)

    def click_submit(self):
       # logger.info("点击 提交")
        self.click(self.Submit_button)

    def click_start(self):
       # logger.info("点击 开始")
        self.click(self.Confirm_button)
