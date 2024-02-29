import xlwings as xw

# Cach 1: file Script va File Excel dang nam chung 1 thu muc
# Terminal: cd C:\Users\ADMIN\Desktop\Python_Excel_Cobra_Team\Bai_08
wb3 = xw.Book('book1_14h09.xlsx')

# Cách 2: Kết nối với file Excel ở vị trí bất kỳ trong máy tính
wb4 = xw.Book(r'C:\Users\ADMIN\Desktop\Python_Excel_Cobra_Team\Bai_08\book2_14h09.xlsx')
