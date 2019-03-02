from base.base_action import BaseAction
from base.base_element import BaseElements


class SettingPage(BaseAction,BaseElements):

    def click_lang(self):
        self.click(self.Language_button)

    def click_notices(self):
        self.click(self.Notices_button)

    def click_PIN_manage(self):

        self.click(self.PIN_manage_button)

    def click_back(self):
        self.click(self.Back_button1)