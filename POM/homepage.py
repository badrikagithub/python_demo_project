from _lib import SeleniumWrapper
from excel_lib import read_locators

# class HomePage:
#
#     def __init__(self,driver):
#         self.driver=driver
#         self.wrapper=SeleniumWrapper(self.driver)
#
#     def register_lnk(self):
#         self.wrapper.click_on_element(("xpath","//a[text()='Register']"))
#
#     def login_lnk(self):
#         self.wrapper.click_on_element(("xpath","//a[.='Log in']"))




##################################################################################################################################################
#optimised the code
# class HomePage:
#     locators={"link_register":(("xpath","//a[text()='Register']"))} #we can create a dict having key =element_name and value=(locator typ ,locator value)
#     #ORR
#     lnk_register=("xpath","//a[text()='Register']")
#     lnk_login=("xpath","//a[.='Log in']")
#
#     def __init__(self,driver):
#         self.driver=driver
#         self.wrapper=SeleniumWrapper(self.driver)
#
#     def register_lnk(self):
#         self.wrapper.click_on_element(self.lnk_register)
#
#     def login_lnk(self):
#         self.wrapper.click_on_element(self.lnk_login)
######################################################################################################################################
#reading locators from excel

# class HomePage:
#     locators=read_locators("homepage") #locators is an dictionary so get the value by using get method of dict get will give the value of the key pass
#
#
#
#     def __init__(self,driver):
#         self.driver=driver
#         self.wrapper=SeleniumWrapper(self.driver)
#
#     def register_lnk(self):
#         self.wrapper.click_on_element(self.locators.get("lnk_register"))
#
#     def login_lnk(self):
#        self.wrapper.click_on_element(self.locators.get("lnk_login"))


##################################################################
#by using class decorator
from excel_lib import attach_locators
@attach_locators("homepage")
class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.wrapper=SeleniumWrapper(self.driver)

    def register_lnk(self):
        self.wrapper.click_on_element(self.lnk_register)

    def login_lnk(self):
        self.wrapper.click_on_element(self.lnk_login)

