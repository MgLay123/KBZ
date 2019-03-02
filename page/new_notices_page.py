from base.base_action import BaseAction
from base.base_element import BaseElements


class NewNoticesPage(BaseAction,BaseElements):

    def click_sound(self):
        self.click(self.Notice_sound_button)

    def click_vibrade(self):
        self.click(self.Notice_vibrate_button)

    def click_back(self):
        self.click(self.Back_button1)
