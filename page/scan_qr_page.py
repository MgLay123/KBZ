from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class ScanQRPage(BaseAction, BaseElements):

    def click_album(self):
        # logger.info("点击 Album")
        self.click(self.Album_button)

    def click_manual(self):
        # logger.info("点击 Manual")
        self.click(self.Manual_button)

    def click_light(self):
        # logger.info("点击 打开灯光")
        self.click(self.light_button)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)
