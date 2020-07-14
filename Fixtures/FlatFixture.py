from appium import webdriver
from Fixtures.BaseAppiumFixture import BaseAppiumFixture
from Locators.FlatLocators import FlatLocators


class FlatFixture(BaseAppiumFixture):
    def __init__(self):
        target = r"https://testpartner.vtbins.ru/mobile/flat/index.php"
        BaseAppiumFixture.__init__(self, target)

    def fill_mobile_frame(self):
        driver = self.driver
        element = driver.find_element_by_xpath(FlatLocators.FlatArea)
        element.send_keys("1")
        # driver.press_keycode(1)
        # driver.press_keycode(0)
        # driver.press_keycode(0)
        # driver.press_keycode(66)

