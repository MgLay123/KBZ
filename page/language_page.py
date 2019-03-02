from base.base_action import BaseAction
from base.base_element import BaseElements


class LanguagePage(BaseAction,BaseElements):

    def click_en(self):
        self.click(self.lang_en)

    def click_ch(self):
        self.click(self.lang_ch)

    def click_my(self):

        self.click(self.lang_my)

    def click_back(self):

        self.click(self.Back_button1)