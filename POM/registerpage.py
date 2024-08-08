from _lib import SeleniumWrapper
# class ResistrationPage:
#     def __init__(self,driver):
#         self.driver=driver
#         self.wrapper=SeleniumWrapper(driver)
#
#     def registrer(self,gender,fname,lname,email,pwd):
#         if gender.upper()=="MALE":
#             self.wrapper.click_on_element(("id","gender-male"))
#         elif gender.upper()=="FEMALE":
#             self.wrapper.click_on_element(("id","gender-female"))
#
#         else:
#             raise Exception("invalid gender")
#
#         self.wrapper.enter_element(("id","FirstName"),value=fname)
#
#         self.wrapper.enter_element(("id","LastName"),value=lname)
#
#         self.wrapper.enter_element(("id","Email"),value=email)
#
#         self.wrapper.enter_element(("id","Password"),value=pwd)
#
#         self.wrapper.enter_element(("id","ConfirmPassword"),value=pwd)
#
#         self.wrapper.click_on_element(("id","register-button"))



###################################################################################################################################
#optimising the locators
# class ResistrationPage:
#     rdo_male = ("id", "gender-male")
#     rdo_female = ("id", "gender-female")
#     txt_fname = ("id", "FirstName")
#     txt_lname = ("id", "LastName")
#     txt_reg_email = ("id", "Email")
#     txt_reg_password = ("id", "Password")
#     txt_confirm_password = ("id", "ConfirmPassword")
#     btn_register = ("id", "register-button")
#
#     def __init__(self,driver):
#         self.driver=driver
#         self.wrapper=SeleniumWrapper(driver)
#
#     def registrer(self,gender,fname,lname,email,pwd):
#         if gender.upper()=="MALE":
#             self.wrapper.click_on_element(self.rdo_male)
#         elif gender.upper()=="FEMALE":
#             self.wrapper.click_on_element(self.rdo_female)
#
#         else:
#             raise Exception("invalid gender")
#
#         self.wrapper.enter_element(self.txt_fname,value=fname)
#
#         self.wrapper.enter_element(self.txt_lname,value=lname)
#
#         self.wrapper.enter_element(self.txt_reg_email,value=email)
#
#         self.wrapper.enter_element(self.txt_reg_password,value=pwd)
#
#         self.wrapper.enter_element(self.txt_confirm_password,value=pwd)
#
#         self.wrapper.click_on_element(self.btn_register)


#########################################################################
#fetch the locators by using excel
from excel_lib import read_locators
# class ResistrationPage:
#     locators=read_locators("registrationpage")
#
#
#     def __init__(self,driver):
#         self.driver=driver
#         self.wrapper=SeleniumWrapper(driver)
#
#     def registrer(self,gender,fname,lname,email,pwd):
#         if gender.upper()=="MALE":
#             self.wrapper.click_on_element(self.locators.get("rdo_male"))
#         elif gender.upper()=="FEMALE":
#             self.wrapper.click_on_element(self.locators.get("rdo_female"))
#
#         else:
#             raise Exception("invalid gender")
#
#         self.wrapper.enter_element(self.locators.get("txt_fname"),value=fname)
#
#         self.wrapper.enter_element(self.locators.get("txt_lname"),value=lname)
#
#         self.wrapper.enter_element(self.locators.get("txt_email"),value=email)
#
#         self.wrapper.enter_element(self.locators.get("txt_password"),value=pwd)
#
#         self.wrapper.enter_element(self.locators.get("txt_confirmpassword"),value=pwd)
#
#         self.wrapper.click_on_element(self.locators.get("btn_register"))

##########################################################################
#by using class decorator

from excel_lib import attach_locators
@attach_locators("registrationpage")
class ResistrationPage:
    def __init__(self,driver):
        self.driver=driver
        self.wrapper=SeleniumWrapper(driver)

    def registrer(self,gender,fname,lname,email,pwd):
        if gender.upper()=="MALE":
            self.wrapper.click_on_element(self.rdo_male)
        elif gender.upper()=="FEMALE":
            self.wrapper.click_on_element(self.rdo_female)

        else:
            raise Exception("invalid gender")

        self.wrapper.enter_element(self.txt_fname,value=fname)

        self.wrapper.enter_element(self.txt_lname,value=lname)

        self.wrapper.enter_element(self.txt_email,value=email)

        self.wrapper.enter_element(self.txt_password,value=pwd)

        self.wrapper.enter_element(self.txt_confirmpassword,value=pwd)

        self.wrapper.click_on_element(self.btn_register)



    