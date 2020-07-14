from appium import webdriver
from Locators.CommonLocators import CommonLocators

class BaseAppiumFixture:
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Pixel_3a_API_30_x86"
    }

    def __init__(self, target):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
        self.target = target

    def open_mobile_page(self):
        driver = self.driver
        element = driver.find_element_by_accessibility_id(CommonLocators.ChromeIcon)
        element.click()
        # driver.implicitly_wait(2)
        # element = driver.find_element_by_id(CommonLocators.SearchBox)
        # element.click()
        # driver.implicitly_wait(2)
        # element = driver.find_element_by_id(CommonLocators.UrlBar)
        # element.send_keys(self.target)
        # driver.press_keycode(66)