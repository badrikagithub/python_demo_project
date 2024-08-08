from typing import Self

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

# from Registration import driver

'''
class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    def enter_element(self, locator: tuple[str, str], value: str):  # locator
        self.driver.find_element(*locator).clear()  # tuple unpacking i.e locator_type,locator_value=locator
        self.driver.find_element(*locator).send_keys(value)

    def click_on_element(self, locator: tuple[str, str]):
        self.driver.find_element(*locator).click()

    def select_element(self, locator: tuple[str, str], textvalue: str):
        ele = self.driver.find_element(*locator)
        select = Select(ele)
        select.select_by_visible_text(textvalue)
'''
# ***************************************************************************************************************************************************************
'''
implements explicit wait as decorator i.t @_wait
'''


def _wait(func):
    def wrapper(instance: Self, locator: tuple[str, str], **kwargs: dict[str, str]):
        w = WebDriverWait(instance.driver, 10)
        print(f'waiting for locator {locator}')
        w.until(visibility_of_element_located(locator))
        return func(instance, locator, **kwargs)

    return wrapper


class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    @_wait
    def enter_element(self, locator: tuple[str, str], *, value: str):  # locator
        self.driver.find_element(*locator).clear()  # tuple unpacking i.e locator_type,locator_value=locator
        self.driver.find_element(*locator).send_keys(value)

    @_wait
    def click_on_element(self, locator: tuple[str, str]):
        self.driver.find_element(*locator).click()

    @_wait
    def select_element(self, locator: tuple[str, str], *, textvalue: str):
        ele = self.driver.find_element(*locator)
        select = Select(ele)
        select.select_by_visible_text(textvalue)



















