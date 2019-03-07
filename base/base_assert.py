import time

from base.base_action import BaseAction


class BaseAssert:

    def if_display(self, driver, text):
        for i in range(10):

            if text in driver.page_source:
                break
            else:
                time.sleep(2)
                print('Finding element，Please waiit...')
                if i == 9:
                    raise Exception("Page load timeout, element lookup failed！")

    def Assert_display(self, driver, text):
        for i in range(6):

            if text in driver.page_source:
                assert True
                print(' Assert Success!')
                break
            else:
                time.sleep(2)
                print('Asserting,Please wait...')
                if i == 5:
                    print('Aseert Failed!')
                    assert False
