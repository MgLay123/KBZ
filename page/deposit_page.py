from base.base_action import BaseAction
from base.base_element import BaseElements
from base.base_logs import Logger
from page import logger


class DepositPage(BaseAction, BaseElements):

    def click_cashin_from_agent(self):
        # logger.info("点击 Cash In From Agent")
        self.click(self.Cashin_from_agent)

    def click_transfer_from_bankAC(self):
        # logger.info("点击 Tranfer From Bank Account")
        self.click(self.Transfer_from_bank_AC)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)
