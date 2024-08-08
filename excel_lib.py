from xlrd import open_workbook



#
# #reading locators for homepage from excel
# book=open_workbook(r"C:\Users\HP\selenium_demo1\BadrikaFramework\POM\page-locators.xls")
# sheet=book.sheet_by_name("homepage")
# get all the used rows in the worksheet
# used_rows=sheet.nrows
# #colmns=sheet.ncols
# print(used_rows)
# #print(colmns)
#
# for row in range(0,used_rows):
#     print(sheet.row_values(row))
#


def read_locators(sheetname):

    book=open_workbook(r"C:\Users\HP\selenium_demo1\BadrikaFramework\POM\page-locators.xls")
    sheet=book.sheet_by_name(sheetname)
    used_rows=sheet.nrows
    data={}
    for i in range(1,used_rows):
        row=sheet.row_values(i)
        data[row[0]]=(row[1],row[2])
    return data

#read_locators("loginpage")

def attach_locators(sheetname):
    def _attact_locators(cls):
        book=open_workbook(r"C:\Users\HP\selenium_demo1\BadrikaFramework\POM\page-locators.xls")
        sheet=book.sheet_by_name(sheetname)
        used_rows=sheet.nrows
        for i in range(1,used_rows):
            row=sheet.row_values(i)

            setattr(cls,row[0],(row[1],row[2]))

        return cls
    return _attact_locators

# book = open_workbook(r"C:\Users\HP\selenium_demo1\BadrikaFramework\testdata.xls")
# sheet = book.sheet_by_name("smoke")
# used_rows = sheet.nrows
# for i in range(0, used_rows):
#     data = sheet.row_values(i)

#     temp_data = [item.strip() for item in data if item.strip()]
#     print(temp_data)

#reading test data

def read_headers(sheet_name,tes_case_name):
    book=open_workbook(r"C:\Users\HP\selenium_demo1\BadrikaFramework\testdata.xls")
    sheet=book.sheet_by_name(sheet_name)
    used_rows=sheet.nrows
    for i in range(0,used_rows):
        row=sheet.row_values(i)
        if row[0]==tes_case_name:
            headers=sheet.row_values(i-1)
            valid_headers=[ headers .strips() for header in headers if header.strip()]
            return ",".join(valid_headers[2:])

def read_data(sheetname,test_case_name):
    book=open_workbook(r"C:\Users\HP\selenium_demo1\BadrikaFramework\testdata.xls")
    sheet=book.sheet_by_name(sheetname)
    used_rows = sheet.nrows
    final_data = []
    temp = []
    for i in range(0,used_rows):
        row=sheet.row_values(i)
        if row[0] == test_case_name:
            temp_record = [item.strip() for item in row if item.strip()]
            if temp_record[1].upper() == "YES":
                final_data.append(tuple(temp_record[2:]))
    return final_data























