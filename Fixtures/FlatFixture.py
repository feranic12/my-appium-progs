from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from Fixtures.BaseAppiumFixture import BaseAppiumFixture
from Locators.FlatLocators import FlatLocators


class FlatFixture(BaseAppiumFixture):
    def __init__(self):
        target = r"https://testpartner.vtbins.ru/mobile/flat/index.php"
        BaseAppiumFixture.__init__(self, target)

    def fill_mobile_frame(self):
        driver = self.driver
        actions = self.actions
        element = driver.find_element_by_xpath(FlatLocators.FlatArea)
        element.send_keys("100")
        element = driver.find_element_by_xpath(FlatLocators.Moscow)
        element.click()
        element = driver.find_element_by_xpath(FlatLocators.OwnYes)
        element.click()
        driver.implicitly_wait(10)
        element = driver.find_element_by_xpath(FlatLocators.RentNo)
        element.click()
        element = driver.find_element_by_xpath(FlatLocators.ConstructionElements)
        element.click()
        driver.implicitly_wait(1)
        element = driver.find_element_by_xpath(FlatLocators.Construction_Million)
        element.click()
        driver.implicitly_wait(1)
        element = driver.find_element_by_xpath(FlatLocators.Button1)
        element.click()