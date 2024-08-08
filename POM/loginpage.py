from _lib import SeleniumWrapper

# class LoginPage:
#     def __init__(self,driver):
#         self.driver=driver
#         self.wrapper=SeleniumWrapper(self.driver)
#
#     def login(self,email,pw):
#         self.wrapper.enter_element(("id","Email"),value=email)
#         self.wrapper.enter_element(("id","Password"),value=pw)
#         self.wrapper.click_on_element(("xpath","//input[@value='Log in']",))


############################################################################################################################
#optimising the locators
# class LoginPage:
#     txt_email = ("id","Email")
#     txt_psw = ("id","Password")
#     btn_login = ("xpath","//input[@value='Log in']")
#
#     def __init__(self,driver):
#         self.driver=driver
#         self.wrapper=SeleniumWrapper(self.driver)
#
#     def login(self,email,pw):
#         self.wrapper.enter_element(self.txt_email,value=email)
#         self.wrapper.enter_element(self.txt_psw,value=pw)
#         self.wrapper.click_on_element(self.btn_login)


#######################################################################################
#by using excel
# from excel_lib import read_locators
# class LoginPage:
#     locators=read_locators("loginpage")
#
#
#
#     def __init__(self,driver):
#         self.driver=driver
#         self.wrapper=SeleniumWrapper(self.driver)
#
#     def login(self,email,pw):
#         self.wrapper.enter_element(self.locators.get("txt_email"),value=email)
#         self.wrapper.enter_element(self.locators.get("txt_password"),value=pw)
#         self.wrapper.click_on_element(self.locators.get("btn_login"))

#passing locators by using class decorator
from excel_lib import attach_locators
@attach_locators("loginpage")
class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.wrapper=SeleniumWrapper(self.driver)

    def login(self,email,pw):
        self.wrapper.enter_element(self.txt_email, value=email)
        self.wrapper.enter_element(self.txt_password,value=pw)
        self.wrapper.click_on_element(self.btn_login)




        




















































































