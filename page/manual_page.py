from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class ManualPage(BaseAction, BaseElements):

    def click_choose_type(self):
        # logger.info("选择交易类型")
        self.click(self.Choose_type)

    def click_choose_merchant(self):
        # logger.info("选择Merchant")
        self.click(self.choose_merchant)

    def click_choose_agent(self):
        # logger.info("选择Agent")
        self.click(self.choose_agent)

    def click_choose_person(self):
        # logger.info("选择Person")
        self.click(self.choose_person)

    def input_code(self,code):
        # logger.info("输入 Short Code")
        self.input(self.Input_code,code)

    def click_enter(self):
        # logger.info("点击 Enter")
        self.click(self.Enter_button)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button)
