from base.base_action import BaseAction
from base.base_element import BaseElements
from base.base_logs import Logger
from page import logger


class CashoutATMPage(BaseAction, BaseElements):

    def click_no_longer_display(self):
        # logger.info("勾选不再显示")
        self.click(self.No_longer_display)

    def click_request_code(self):
        # logger.info("点击Request Code")
        self.click(self.Request_code)

    def click_search_ATM(self):
        # logger.info("点击Search ATM")
        self.click(self.Search_ATM)

    def click_back(self):
        # logger.info("点击返回")
        self.click(self.Back_button1)
