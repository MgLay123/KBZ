from base.base_action import BaseAction
from base.base_element import BaseElements


class ManualPage(BaseAction, BaseElements):

    def click_choose_type(self):
        self.click(self.Choose_type)

    def click_choose_merchant(self):
        self.click(self.choose_merchant)

    def click_choose_agent(self):
        self.click(self.choose_agent)

    def click_choose_person(self):
        self.click(self.choose_person)

    def input_code(self,code):
        self.input(self.Input_code,code)

    def click_enter(self):
        self.click(self.Enter_button)

    def click_back(self):
        self.click(self.Back_button)
