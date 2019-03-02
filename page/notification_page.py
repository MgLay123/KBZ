from base.base_action import BaseAction
from base.base_element import BaseElements


class NotificationPage(BaseAction, BaseElements):

    def click_sys_info(self):
        self.click(self.Sys_info_button)

    def click_trans_message(self):
        self.click(self.Transation_button)

    def click_news(self):
        self.click(self.News_button)

    def click_back(self):
        self.click(self.Back_button1)
