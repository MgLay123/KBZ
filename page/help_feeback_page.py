from base.base_action import BaseAction
from base.base_element import BaseElements


class HelpFeebackPage(BaseAction, BaseElements):

    def click_help(self):
        self.click(self.Help_button)

    def click_feeback(self):
        self.click(self.Feeback_button)

    def click_FAQ(self):
        self.click(self.FAQ_button)

    def click_back(self):
        self.click(self.Back_button1)
