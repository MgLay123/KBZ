import time
from base.base_element import BaseElements
from base.base_login import login


class TestNotify(BaseElements):

    def setup(self):
        self.page, self.driver = login()

    def test_sys_notify(self):
        self.page.banner_page.click_notification()
        self.page.notification_page.click_sys_info()
        time.sleep(3)
        self.page.notification_page.click_back()

        self.page.notification_page.click_trans_message()
        time.sleep(3)
        self.page.notification_page.click_back()

        self.page.notification_page.click_news()
        time.sleep(3)
        self.page.notification_page.click_back()

    def teardown(self):
        time.sleep(2)
        self.driver.quit()
