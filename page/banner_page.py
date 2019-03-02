from base.base_action import BaseAction
from base.base_element import BaseElements


class BannerPage(BaseAction, BaseElements):

    def click_drawer(self):
        self.click(self.drawer_button)

    def click_notification(self):
        self.click(self.notification_button)

    def click_balance(self):
        self.click(self.balance_button)

    def click_scanQR(self):
        self.click(self.scanQR_button)

    def click_QR(self):
        self.click(self.QR_button)

    def click_CashIn(self):
        self.click(self.CashIn_button)

    def click_CashOut(self):
        self.click(self.CashOut_button)

    def click_Gift(self):
        self.click(self.Gift_button)

    def click_Nearby(self):
        self.click(self.Nearby_button)

    def click_Tansfer(self):
        self.click(self.Transfer_button)

    def click_Topup(self):
        self.click(self.Topup_button)

    def click_Bankaccount(self):
        self.click(self.Bank_account_button)

    def click_QuickPay(self):
        self.click(self.QuickPay_button)

    def click_History(self):
        self.click(self.History_button)
