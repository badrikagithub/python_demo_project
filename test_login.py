from selenium.webdriver.chrome.webdriver import WebDriver

from _lib import SeleniumWrapper
from POM.homepage import HomePage
from POM.loginpage import LoginPage



# def test_login(driver,_config):
#     # driver = WebDriver()
#     # driver.get("https://demowebshop.tricentis.com/")
#     # driver.maximize_window()
#
#     wrapper = SeleniumWrapper(driver)
#
#     wrapper.click_on_element(("xpath", "//a[.='Log in']"))
#     wrapper.enter_element(("id", "Email"), value=_config.email)
#     wrapper.enter_element(("id", "Password"), value=_config.email)
#     wrapper.click_on_element(("xpath", "//input[@value='Log in']"))
#     #driver.close()

#####################################################################################################################################################
'''
BY USING POM CLASS

'''
# def test_login(driver):
#     hp=HomePage(driver)
#     hp.login_lnk()
#
#     lp=LoginPage(driver)
#     lp.login("julie.mbj@gmail.com","password123")


####################################################################
'''
Using "pages" fixture 
 page fixture reyurn the obj instace og each page ..so we can call the methods present
 in the respective pages by using the instance

'''
def test_login(driver,_config,pages):
    pages.hpage.login_lnk()
    pages.lpage.login(_config.email,_config.password)















