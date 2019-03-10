import time

from base.base_action import BaseAction
from page import logger


class BaseAssert:

    def if_display(self, driver, text):
        for i in range(10):

            if text in driver.page_source:
                logger.info("指定文本在界面出现，进行下一步操作！")
                break
            else:
                time.sleep(2)
                logger.info("指定文本在界面未出现，准备重试！")
                if i == 9:
                    raise Exception("Page load timeout, element lookup failed！")

    def Assert_display(self, driver, text):
        for i in range(6):

            if text in driver.page_source:
                assert True
                logger.info("结果断言成功！")
                break
            else:
                time.sleep(2)
                print('Asserting,Please wait...')
                if i == 5:
                    logger.info("结果断言失败！")
                    assert False
