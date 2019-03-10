from base.base_action import BaseAction
from base.base_element import BaseElements
from base.base_logs import Logger
from page import logger


class BannerPage(BaseAction, BaseElements):

    def click_drawer(self):
        # logger.info("点击侧边栏")
        self.click(self.drawer_button)

    def click_notification(self):
        # logger.info("点击提示铃铛")
        self.click(self.notification_button)

    def click_balance(self):
        # logger.info("点击Banlance")
        self.click(self.balance_button)

    def click_scanQR(self):
        # logger.info("点击SCan QRCode")
        self.click(self.scanQR_button)

    def click_QR(self):
        # logger.info("点击二维码")
        self.click(self.QR_button)

    def click_CashIn(self):
        # logger.info("点击Cash In")
        self.click(self.CashIn_button)

    def click_CashOut(self):
        # logger.info("点击SCan Cash Out")
        self.click(self.CashOut_button)

    def click_Gift(self):
        # logger.info("点击Gift")
        self.click(self.Gift_button)

    def click_Nearby(self):
        # logger.info("点击NearBy")
        self.click(self.Nearby_button)

    def click_Tansfer(self):
        # logger.info("点击Transfer")
        self.click(self.Transfer_button)

    def click_Topup(self):
        # logger.info("点击TopUp")
        self.click(self.Topup_button)

    def click_Bankaccount(self):
        # logger.info("点击Bank Account")
        self.click(self.Bank_account_button)

    def click_QuickPay(self):
        # logger.info("点击Quick Pay")
        self.click(self.QuickPay_button)

    def click_History(self):
        # logger.info("点击History")
        self.click(self.History_button)
