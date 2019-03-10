from base.base_action import BaseAction
from base.base_element import BaseElements
from base.base_logs import Logger
from page import logger


class HistoryPage(BaseAction, BaseElements):

    def click_filtrate(self):
        # logger.info("点击 日历")
        self.click(self.Filtrate_img)

    def input_minimum(self,minimum):
        # logger.info("输入 最小金额")
        self.input(self.Min_amount,minimum)

    def input_maximum(self,maximum):
        # logger.info("输入 最大金额")
        self.input(self.Max_amount,maximum)

    def click_reset(self):
        # logger.info("点击 Reset")
        self.click(self.Reset_filtrate)

    def click_confirm(self):
        # logger.info("点击 确定")
        self.click(self.Confirm_filtrate)

    def click_date(self):
        # logger.info("点击 日期")
        self.click(self.Date_img)

    def click_from_time(self):
        # logger.info("输入 起始日期")
        self.click(self.From_time)
    def click_end_time(self):
        # logger.info("输入 结束日期")
        self.click(self.End_time)

    def click_ok(self):
        # logger.info("点击 OK")
        self.click(self.Bt_OK)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)
