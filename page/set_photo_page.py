from base.base_action import BaseAction
from base.base_element import BaseElements


class SetphotoPage(BaseAction,BaseElements):

    def click_take_photo(self):
        self.click(self.take_photo_button)

    def click_choose_photo(self):
        self.click(self.choose_photo_button)

    def click_back(self):
        self.click(self.Back_button1)