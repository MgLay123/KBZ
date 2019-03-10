from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class NewNoticesPage(BaseAction,BaseElements):

    def click_sound(self):
        # logger.info("点击 声音")
        self.click(self.Notice_sound_button)

    def click_vibrade(self):
        # logger.info("点击 Vibrade")
        self.click(self.Notice_vibrate_button)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)
