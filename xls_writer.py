##############################################################################
#
# A simple example of converting a Pandas dataframe to an xlsx file using
# Pandas and XlsxWriter.
#
# Copyright 2013-2020, John McNamara, jmcnamara@cpan.org
#

import pandas as pd

# Create a Pandas dataframe from some data.
df1 = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
df2 = pd.DataFrame({'Data': [21, 22, 23, 24]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df1.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Apply a conditional format to the cell range.
# Adds colouring to values
worksheet.conditional_format('B2:B8', {'type': '3_color_scale'})

# Create a chart object.
chart = workbook.add_chart({'type': 'column'})

# Configure the series of the chart from the dataframe data.
chart.add_series({'values': '=Sheet1!$B$2:$B$8'})

# Insert the chart into the worksheet.
worksheet.insert_chart('D2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()