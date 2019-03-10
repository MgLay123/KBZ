from page.balance_page import BalancePage
from page.bank_account_page import BankAccountPage
from page.banner_page import BannerPage
from page.cash_in_page import CashinPage
from page.cash_out_ATM_page import CashoutATMPage
from page.cash_out_page import CashoutPage
from page.change_pin_page import ChangePinPage
from page.deposit_page import DepositPage
from page.forget_pin_page import ForgetPinPage
from page.help_feeback_page import HelpFeebackPage
from page.history_page import HistoryPage
from page.language_page import LanguagePage
from page.login_page import LoginPage
from page.manual_page import ManualPage
from page.nearby_page import NearByPage
from page.new_notices_page import NewNoticesPage
from page.notification_page import NotificationPage
from page.payment_page import PaymentPage
from page.pin_enter_page import PinEnterPage
from page.pin_manage_page import PinManagePage
from page.qr_recevie_page import ReceivePage
from page.quick_pay_page import QuickPayPage
from page.reset_pin_page import ResetPinPage
from page.scan_qr_page import ScanQRPage
from page.set_photo_page import SetphotoPage
from page.setting_page import SettingPage
from page.sidebar_page import SidebarPage
from page.top_up_page import TopUpPage
from page.transfer_page import TransferPage
from page.withdraw_page import WithDrawPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def login_page(self):

        return LoginPage(self.driver)

    @property
    def banner_page(self):
        return BannerPage(self.driver)

    @property
    def sidebar_page(self):
        return SidebarPage(self.driver)

    @property
    def setting_page(self):
        return SettingPage(self.driver)

    @property
    def language_page(self):
        return LanguagePage(self.driver)

    @property
    def new_notices_page(self):
        return NewNoticesPage(self.driver)

    @property
    def pin_manage_page(self):
        return PinManagePage(self.driver)

    @property
    def change_pin_page(self):
        return ChangePinPage(self.driver)

    @property
    def forget_pin_page(self):
        return ForgetPinPage(self.driver)

    @property
    def set_photo_page(self):
        return SetphotoPage(self.driver)

    @property
    def reset_pin_page(self):
        return ResetPinPage(self.driver)

    @property
    def help_feeback_page(self):
        return HelpFeebackPage(self.driver)

    @property
    def notification_page(self):
        return NotificationPage(self.driver)

    @property
    def balance_page(self):
        return BalancePage(self.driver)

    @property
    def deposit_page(self):
        return DepositPage(self.driver)

    @property
    def scanqr_page(self):
        return ScanQRPage(self.driver)

    @property
    def manual_page(self):
        return ManualPage(self.driver)

    @property
    def qr_receive_page(self):
        return ReceivePage(self.driver)

    @property
    def cash_in_page(self):
        return CashinPage(self.driver)

    @property
    def cash_out_page(self):
        return CashoutPage(self.driver)

    @property
    def cash_out_ATM_page(self):
        return CashoutATMPage(self.driver)

    @property
    def pin_enter_page(self):
        return PinEnterPage(self.driver)

    @property
    def top_up_page(self):
        return TopUpPage(self.driver)

    @property
    def nearby_page(self):
        return NearByPage(self.driver)

    @property
    def transfer_page(self):
        return TransferPage(self.driver)

    @property
    def history_page(self):
        return HistoryPage(self.driver)

    @property
    def quick_pay_page(self):
        return QuickPayPage(self.driver)

    @property
    def bank_account_page(self):
        return BankAccountPage(self.driver)

    @property
    def withdraw_page(self):
        return WithDrawPage(self.driver)
    @property
    def payment_page(self):
        return PaymentPage(self.driver)