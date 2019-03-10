from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class SetphotoPage(BaseAction,BaseElements):

    def click_take_photo(self):
        # logger.info("点击 照相")
        self.click(self.take_photo_button)

    def click_choose_photo(self):
        # logger.info("点击 选择相片")
        self.click(self.choose_photo_button)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)