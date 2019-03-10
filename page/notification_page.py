from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class NotificationPage(BaseAction, BaseElements):

    def click_sys_info(self):
        # logger.info("点击 系统信息")
        self.click(self.Sys_info_button)

    def click_trans_message(self):
        # logger.info("点击 交易信息")
        self.click(self.Transation_button)

    def click_news(self):
        # logger.info("点击 新闻")
        self.click(self.News_button)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)
