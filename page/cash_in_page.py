from base.base_action import BaseAction
from base.base_element import BaseElements
from base.base_logs import Logger
from page import logger


class CashinPage(BaseAction, BaseElements):

    def click_agent(self):
        # logger.info("点击Agent")
        self.click(self.Agent)

    def click_bank_ac(self):
        # logger.info("点击Bank Account")
        self.click(self.Bank_account)

    def click_no_longer_display(self):
        # logger.info("勾选No Longer Display")
        self.click(self.No_longer_display)

    def click_start(self):
        # logger.info("点击确定")
        self.click(self.Confirm_button)

    def click_back(self):
        # logger.info("点击返回")
        self.click(self.Back_button1)
