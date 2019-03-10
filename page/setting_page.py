from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class SettingPage(BaseAction,BaseElements):

    def click_lang(self):
        # logger.info("点击 语言")
        self.click(self.Language_button)

    def click_notices(self):
        # logger.info("点击 提示")
        self.click(self.Notices_button)

    def click_PIN_manage(self):
        # logger.info("点击 密码管理")

        self.click(self.PIN_manage_button)

    def click_back(self):
        # logger.info("点击 返回")
        self.click(self.Back_button1)