from base.base_action import BaseAction
from base.base_element import BaseElements
from base.base_logs import Logger
from page import logger


class HelpFeebackPage(BaseAction, BaseElements):

    def click_help(self):
        # logger.info("点击 Help")
        self.click(self.Help_button)

    def click_feeback(self):
        # logger.info("点击 FeedBack")
        self.click(self.Feeback_button)

    def click_FAQ(self):
        # logger.info("点击 FAQ")
        self.click(self.FAQ_button)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)
