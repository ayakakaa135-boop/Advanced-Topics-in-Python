import openpyxl
from pathlib import Path
from openpyxl.chart import Reference, BarChart

# حطي اسم الملف اللي بدك إياه هنا
file_name = "custom_chart.xlsx"  # غيري الاسم حسب رغبتك
folder_path = r"C:\Users\haama\Desktop\PycharmProjects\Advanced Topics in Python\Excel"
file_path = Path(folder_path) / file_name

# إنشاء ملف Excel جديد
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "sheet1"

# إضافة بيانات تجريبية
data_rows = [
    ["Item", "Value"],
    ["A", 10],
    ["B", 20],
    ["C", 30],
    ["D", 40],
    ["E", 50],
]
for row in data_rows:
    sheet.append(row)

# تحديد نطاق البيانات للرسم البياني
data = Reference(sheet, min_col=2, max_col=2, min_row=1, max_row=6)
titles = Reference(sheet, min_col=1, max_col=1, min_row=2, max_row=6)

# إنشاء الرسم البياني
chart = BarChart()
chart.add_data(data, titles_from_data=True)
chart.set_categories(titles)
chart.title = "Example Chart"
chart.x_axis.title = "X Axis"
chart.y_axis.title = "Y Axis"

# وضع الرسم البياني في ورقة العمل
sheet.add_chart(chart, "E5")

# حفظ الملف
wb.save(file_path)
print("File created:", file_path)
