from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.analysis_data import AnalysisData
from page import logger


class BaseAction:

    def __init__(self, driver):

        self.driver = driver

    def find_element(self, feature, timeout=60, poll_frequency=0.5):

        by, value = feature
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(by, value))

    def click(self, feature):

        self.find_element(feature).click()
        dict = AnalysisData("name_data").analysis_base_data()
        for i in dict:
            new_dict = {v: k for k, v in i.items()}
            name_click = new_dict[feature[1]]
            info = "点击" + name_click + "按钮"
            logger.info(info)

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)
        dict = AnalysisData("name_data").analysis_base_data()
        for i in dict:
            new_dict = {v: k for k, v in i.items()}
            name_click = new_dict[feature[1]]

            info = "在输入框中输入"+name_click.split('_', 1)[1]
            logger.info(info)

    def find_toast(self, toast_text, poll_frequency=0.1):
        message = By.XPATH, "//*[contains(@text,'" + toast_text + "')]"
        return self.find_element(message, timeout=10, poll_frequency=poll_frequency).text

    def move_and_click(self, feature):

        while True:

            try:
                self.find_element(feature, timeout=4)
                return self.find_element(feature).click()


            except:

                TouchAction(self.driver).press(x=700, y=2500).wait(1000).move_to(x=700, y=2000).release().perform()

    def move_and_input(self, feature, text):

        while True:

            try:
                self.find_element(feature, timeout=4)
                return self.find_element(feature).send_keys(text)


            except:

                TouchAction(self.driver).press(x=700, y=2500).wait(1000).move_to(x=700, y=2000).release().perform()

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
