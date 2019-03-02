from base.base_action import BaseAction
from base.base_element import BaseElements


class HistoryPage(BaseAction, BaseElements):

    def click_filtrate(self):

        self.click(self.Filtrate_img)

    def input_minimum(self,minimum):
        self.input(self.Min_amount,minimum)

    def input_maximum(self,maximum):
        self.input(self.Max_amount,maximum)

    def click_reset(self):
        self.click(self.Reset_filtrate)

    def click_confirm(self):
        self.click(self.Confirm_filtrate)

    def click_date(self):
        self.click(self.Date_img)

    def click_from_time(self):
        self.click(self.From_time)
    def click_end_time(self):
        self.click(self.End_time)

    def click_ok(self):
        self.click(self.Bt_OK)

    def click_back(self):
        self.click(self.Back_button1)
