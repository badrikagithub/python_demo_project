from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from pytest import mark


from _lib import SeleniumWrapper
from POM.homepage import HomePage
from POM.registerpage import ResistrationPage


from selenium.webdriver.support.select import Select


# driver = WebDriver()
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()

# def enter_element(locator_type,locator_value,value):#locator
#     driver.find_element(locator_type,locator_value).clear()
#     driver.find_element(locator_type,locator_value).send_keys(value)
#
# def click_on_element(locator_type,locator_value):
#     driver.find_element(locator_type,locator_value).click()
#
# def select_element(locator_type,locator_value,textvalue):
#     ele=driver.find_element(locator_type,locator_value)
#     select=Select(ele)
#     select.select_by_visible_text(textvalue)
############################################################################################################################################################
# BY USING UNPACKING
# def enter_element(locator:tuple[str,str],value:str):#locator
#     driver.find_element(*locator).clear() #tuple unpacking i.e locator_type,locator_value=locator
#     driver.find_element(*locator).send_keys(value)
#
# def click_on_element(locator:tuple[str,str]):
#     driver.find_element(*locator).click()
#
# def select_element(locator:tuple[str,str],textvalue:str):
#     ele=driver.find_element(*locator)
#     select=Select(ele)
#     select.select_by_visible_text(textvalue)

#wrapper = SeleniumWrapper(driver)


#def test_registration(driver):
            #apply this by using fixture
            # driver = WebDriver()
            # driver.get("https://demowebshop.tricentis.com/")
            # driver.maximize_window()

            # wrapper = SeleniumWrapper(driver)
            #
            # # driver.find_element("xpath","//a[text()='Register']").click()
            # wrapper.click_on_element(("xpath", "//a[text()='Register']"))
            #
            # # driver.find_element("id","gender-female").click()
            # wrapper.click_on_element(("id", "gender-female"))
            #
            # # driver.find_element("id","FirstName").send_keys("Badrika")
            # wrapper.enter_element(("id", "FirstName"), value="Badrika")
            #
            # # driver.find_element("id","LastName").send_keys("Mohanta")
            # wrapper.enter_element(("id", "LastName"),value="Mohanta")
            #
            # # driver.find_element("id","Email").send_keys("badrika123@gmail.com")
            # wrapper.enter_element(("id", "Email"),value="badrika123@gmail.com")
            #
            # # driver.find_element("id","Password").send_keys("Password45")
            # wrapper.enter_element(("id", "Password"),value="Password45")
            #
            # # driver.find_element("id","ConfirmPassword").send_keys("Password45")
            # wrapper.enter_element(("id", "ConfirmPassword"),value="Password45")
            #
            # # driver.find_element("id","register-button").click()
            # wrapper.click_on_element(("id", "register-button"))



# driver.close()



###############################################################################################################################################################
'''
SCRIPTING BY USING POM CLASS 
'''
# def test_registration(driver):
#     hp = HomePage(driver)
#     hp.register_lnk()
#
#     rp=ResistrationPage(driver)
#     rp.registrer("male", "julie", "mohanta", "julie.mbj@gmail.com", "password123")

#####################################################################
'''
by using pages fixture and here we hard code the data ,in oder to avoid this he hv to use mark fixture

'''
# def test_registration(driver,pages):
#     pages.hpage.register_lnk()
#     pages.rpage.registrer("male", "julie", "mohanta", "julie.mbj" "@gmail.com", "password123")


#parameterisation /data provider by using MARKER fixture in the test method and we hv to import the mark.

from pytest import mark

headers="gender,fname,lname,email,password"
data=[('male','jobs','steve','jobs.steve@gmail.com','password123'),
      ('female','julie','mohanta','julie.mbj@gmail.com','password123')
      ]

@mark.parametrize(headers,data)
def test_registration(driver,pages,gender,fname,lname,email,password):
    pages.hpage.register_lnk()
    pages.rpage.registrer(gender,fname,lname,email,password)



