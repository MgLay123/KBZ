from base.base_action import BaseAction
from base.base_element import BaseElements
from base.base_logs import Logger
from page import logger


class CashoutPage(BaseAction, BaseElements):

    def click_no_longer_display(self):
        
        # logger.info("勾选不再显示")
        self.click(self.No_longer_display)

    def click_at_agent(self):
        # logger.info("点击At Agent")
        self.click(self.At_agent)

    def input_agent_short_code(self, short_code):
        # logger.info("输入Agent的Short Code")
        self.input(self.Edit_agent, short_code)

    def click_scan_agent(self):
        # logger.info("点击Scan Agent")
        self.click(self.Scan_agent)

    def click_next(self):
        # logger.info("点击Next")
        self.click(self.Next_button)

    def click_MMK(self):
        # logger.info("选择800MMK")
        self.click(self.MMK800)

    def input_amout(self, amount):
        # logger.info("输入金额")
        self.input(self.Other_amount, amount)

    def click_cashout_all(self):
        # logger.info("点击 Cash Out All")
        self.click(self.Cashout_all)

    def click_submit(self):
        # logger.info("点击 Summit")
        self.click(self.Submit_button)

    def click_locate_agent(self):
        # logger.info("点击定位Agent")
        self.click(self.Find_agent_map)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)
