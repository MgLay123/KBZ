from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class ReceivePage(BaseAction, BaseElements):

    def click_set_amount(self):
        # logger.info("点击 设置金额")
        self.click(self.Set_Amount)

    def click_save_image(self):
        # logger.info("点击 保存二维码")
        self.click(self.Save_image)

    def input_amount(self, amount):
        # logger.info("输入 金额")
        self.input(self.Edit_amount, amount)

    def input_note(self, note):
        # logger.info("输入 Notes")
        self.input(self.Add_note, note)

    def click_confirm(self):
        # logger.info("点击 确定")
        self.click(self.Confirm_button1)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)
