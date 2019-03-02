from base.base_action import BaseAction
from base.base_element import BaseElements


class ScanQRPage(BaseAction, BaseElements):

    def click_album(self):
        self.click(self.Album_button)

    def click_manual(self):
        self.click(self.Manual_button)

    def click_light(self):
        self.click(self.light_button)

    def click_back(self):
        self.click(self.Back_button1)
