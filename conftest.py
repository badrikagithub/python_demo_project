#from selenium.webdriver.chrome.webdriver import WebDriver
from pytest import fixture
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from POM.loginpage import LoginPage
from POM.homepage import HomePage
from POM.registerpage import ResistrationPage



# @fixture()
# def _confi():
#     print("executing through fixture")
#     return 1000
env="stage"
browser = "chrome"
@fixture
def _config():

     class TestConfigurations:
          url = "https://demowebshop.tricentis.com/"
          email = "badrika123@gmail.com"
          password = "Password45"

     class StageConfigurations:
          url = "https://demowebshop.tricentis.com/"
          email = "badrika123@gmail.com"
          password = "Password45"

     if env.upper() == "TEST":
          print("Execution environment is TEST")
          return TestConfigurations()
     elif env.upper() == "STAGE":
          print("Execution Environment is STAGE")
          return StageConfigurations()
     else:
          raise Exception("Invalid execution environment")



@fixture
def driver(_config): #passing one fixture to another fixture
     print("executing setup")
     if browser.upper() == "CHROME":
          _driver = Chrome()
     elif browser.upper() == "FIREFOX":
          _driver = Firefox()
     elif browser.upper() == "EDGE":
          _driver = "Edge"
     else:
          raise Exception("Invalid Browser")
     _driver.get(_config.url)
     _driver.maximize_window()
     yield _driver
     print("executing tear down")
     _driver.quit()



@fixture
def pages(driver):

     class Pages:
          hpage=HomePage(driver)
          rpage=ResistrationPage(driver)
          lpage=LoginPage(driver)


     return Pages()


