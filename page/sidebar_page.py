from base.base_action import BaseAction
from base.base_element import BaseElements


class SidebarPage(BaseAction, BaseElements):

    def click_photo(self):
        self.click(self.photo_buttton)

    def click_ibfo(self):
        self.click(self.info_button)

    def click_limit(self):
        self.click(self.limit_button)

    def click_setting(self):
        self.click(self.Setting_button)

    def click_help(self):
        self.click(self.Help_button)

    def click_about(self):
        self.click(self.About_button)

    def click_share(self):
        self.click(self.Share_button)

    def click_logout(self):
        self.click(self.Logout_button)

    def click_cancel(self):
        self.click(self.Logout_cancel)

    def click_confirm(self):
        self.click(self.Logout_confirm)