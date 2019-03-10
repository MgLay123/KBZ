from base.base_action import BaseAction
from base.base_element import BaseElements


class BalancePage(BaseAction, BaseElements):

    def click_withdraw(self):
        # logger.info("点击Withdraw")
        self.click(self.withdraw_button)

    def click_deposit(self):
        # logger.info("Desposit")
        self.click(self.deposit_button)

    def click_history(self):
        # logger.info("点击历史")
        self.click(self.History_button)

    def click_back(self):
        # logger.info("点击返回")
        self.click(self.Back_button1)
