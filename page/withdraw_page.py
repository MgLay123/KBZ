from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class WithDrawPage(BaseAction, BaseElements):

    def click_cashout_from_agent(self):
       # logger.info("点击 Cash Out From Agent")
        self.click(self.CashOut_agent)

    def click_cashout_from_ATM(self):
       # logger.info("点击 CashOut From ATM")
        self.click(self.CashOut_from_ATM)

    def click_transfer_from_bank_AC(self):
       # logger.info("点击 transfer to BankAC")
        self.click(self.Transfer_from_bank_AC)

    def click_back(self):
       # logger.info("点击 返回")
        self.click(self.Back_button1)
