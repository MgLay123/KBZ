from base.base_action import BaseAction
from base.base_element import BaseElements


class LoginPage(BaseAction, BaseElements):

    def click_lang_button(self):
        self.click(self.lang_button)

    def click_en_button(self):
        self.click(self.lang_en)

    def click_my_button(self):
        self.click(self.lang_my)

    def click_ch_button(self):
        self.click(self.lang_ch)

    def click_sidebar(self):
        self.click(self.sidebar_button)

    def click_sidebar_nearby(self):
        self.click(self.sidebar_nearby)

    def click_sidebar_feeback(self):
        self.click(self.sidebar_feeback)

    def click_sidebar_about(self):
        self.click(self.sidebar_about)

    def input_phoneNO(self, phoneNO):
        self.input(self.phoneNO_input, phoneNO)

    def input_smscode(self, smscode):
        self.input(self.sms_input, smscode)

    def click_getcode(self):
        self.click(self.getcode_button)

    def click_start(self):
        self.click(self.start_button)

    def find_start(self):
        return self.find_element(self.start_button).text

    def start_status(self):
        return self.find_element(self.start_button_status)

    def find_title(self):
        return self.find_element(self.title)

    def find_start_status(self, name):
        return self.find_element(self.start_button).get_attribute(name)

    def find_code_status(self, name):
        return self.find_element(self.getcode_button).get_attribute(name)

    def click_term(self):
        self.click(self.agreement_select)
