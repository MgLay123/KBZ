from base.base_action import BaseAction
from base.base_element import BaseElements
from page import logger


class SidebarPage(BaseAction, BaseElements):

    def click_photo(self):
        # logger.info("点击 相片")
        self.click(self.photo_buttton)

    def click_info(self):
        # logger.info("点击 信息")
        self.click(self.info_button)

    def click_limit(self):
        # logger.info("点击 Limit Rule")
        self.click(self.limit_button)

    def click_setting(self):
        # logger.info("点击 设置")
        self.click(self.Setting_button)

    def click_help(self):
        # logger.info("点击 帮助")
        self.click(self.Help_button)

    def click_about(self):
        self.click(self.About_button)

    def click_share(self):
        # logger.info("点击 分享")
        self.click(self.Share_button)

    def click_logout(self):
        # logger.info("点击 登出")
        self.click(self.Logout_button)

    def click_cancel(self):
        # logger.info("点击 取消")
        self.click(self.Logout_cancel)

    def click_confirm(self):
        # logger.info("点击 确定")
        self.click(self.Logout_confirm)