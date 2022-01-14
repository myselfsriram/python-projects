import openpyxl
wb=openpyxl.load_workbook("account.xlsx")
ws=wb['Sheet1']
ws ['A1'] = 'User name'
wb.save("account.xlsx")
print("entered")