from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.analysis_data import AnalysisData
from page import logger


class BaseAction:

    def __init__(self, driver):

        self.driver = driver

    #  每一种不同的点击事件日志打印都需要调用该方法
    def click_log(self, feature):
        dict = AnalysisData("name_data").analysis_base_data()
        for i in dict:
            new_dict = {v: k for k, v in i.items()}
            name_click = new_dict[feature[1]]
            info = "点击" + name_click + "按钮"
            return logger.info(info)

    #  每一种不同的输入事件日志打印都需要调用该方法
    def input_log(self, feature, text):
        dict = AnalysisData("name_data").analysis_base_data()
        for i in dict:
            new_dict = {v: k for k, v in i.items()}
            name_click = new_dict[feature[1]]
            info = "在" + name_click + "输入框中输入" + text
            return logger.info(info)

    #   点击坐标方法
    def click_coordinate(self, coordinate):

        x, y = coordinate

        TouchAction(self.driver).tap(x=x, y=y).perform().release()

    #   重新封装find element 方法
    def find_element(self, feature, timeout=60, poll_frequency=0.5):

        by, value = feature
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(by, value))

    # 重新封装点击方法  加入点击日志打印
    def click(self, feature):

        self.find_element(feature).click()
        self.click_log(feature)

    # 重新封装input方法  加入点击日志打印
    def input(self, feature, text):
        self.find_element(feature).send_keys(text)
        self.input_log(feature, text)

    #   封装找Toast方法
    def find_toast(self, toast_text, poll_frequency=0.1):
        message = By.XPATH, "//*[contains(@text,'" + toast_text + "')]"
        return self.find_element(message, timeout=10, poll_frequency=poll_frequency).text

    # 滑动点击方法
    def move_and_click(self, feature):

        while True:

            try:
                self.find_element(feature, timeout=4)
                self.click_log(feature)
                return self.find_element(feature).click()


            except:
                info = "向上滑动寻找元素"
                logger.info(info)
                TouchAction(self.driver).press(x=700, y=2500).wait(1000).move_to(x=700, y=2000).release().perform()

    # 左滑点击方法
    def move_left_click(self, feature):

        while True:

            try:
                self.find_element(feature, timeout=4)
                self.click_log(feature)
                return self.find_element(feature).click()
            except:
                info = "左滑一次屏幕"
                logger.info(info)
                TouchAction(self.driver).press(x=1200, y=2500).wait(1000).move_to(x=200, y=2500).release().perform()

    # 滑动找到元素后进行输入
    def move_and_input(self, feature, text):

        while True:

            try:
                self.find_element(feature, timeout=4)
                self.input_log(feature, text)
                return self.find_element(feature).send_keys(text)


            except:
                info = "向上滑动寻找元素"
                logger.info(info)
                TouchAction(self.driver).press(x=700, y=2500).wait(1000).move_to(x=700, y=2000).release().perform()

    #  点击后使用键盘输入方法
    def click_and_input(self, a, b, str):
        TouchAction(self.driver).tap(x=a, y=b).perform()

        for i in list(str):
            if i.isdigit():
                i = int(i)
                i += 7
                self.driver.press_keycode(keycode=i)
            elif i.isalpha():
                asc = ord(i)
                code = asc - 68
                self.driver.press_keycode(keycode=code)
            # keycode['@'] = '77'
            # keycode['#'] = '18'
            # keycode['+'] = '81'
            # keycode['-'] = '69'
            # keycode['*'] = '17'
            # keycode['/'] = '76'
            # keycode['='] = '70

            elif i == '-':
                self.driver.press_keycode(69)

            elif i == '+':
                self.driver.press_keycode(81)
