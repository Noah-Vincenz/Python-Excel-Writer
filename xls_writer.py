import pandas as pd
import mysql.connector as mysql
import os
from dotenv import load_dotenv
import kumulativ_writer, dieser_monat_writer, risikokennzahlen_vola_writer

load_dotenv()

db = mysql.connect(
  host=os.getenv('HOST'),
  user=os.getenv('USERNAME'),
  password=os.getenv('PASSWORD'),
  database=os.getenv('DATABASE')
)
print("Connected to:", db.get_server_info())

cursor = db.cursor()

# Create Pandas Excel writer using XlsxWriter engine
writer = pd.ExcelWriter('valor.xlsx', engine='xlsxwriter', options={'strings_to_numbers': True})

kumulativ_writer.write(cursor, writer)
dieser_monat_writer.write(cursor, writer)
risikokennzahlen_vola_writer.write(cursor, writer)

# # Get the xlsxwriter workbook and worksheet objects.
# workbook  = writer.book
# worksheet = writer.sheets['kumulativ']

# # Apply a conditional format to the cell range.
# # Adds colouring to values
# worksheet.conditional_format('C2:C3', {'type': '3_color_scale'})

# # Create a chart object.
# chart = workbook.add_chart({'type': 'column'})

# # Configure the series of the chart from the dataframe data.
# chart.add_series({'values': '=kumulativ!$C$2:$C$3'})

# # Insert the chart into the worksheet.
# worksheet.insert_chart('F10', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
