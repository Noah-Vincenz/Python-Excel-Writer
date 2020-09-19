import pandas as pd
import mysql.connector as mysql
import os
from dotenv import load_dotenv
import kumulativ_writer, dieser_monat_writer, risikokennzahlen_vola_writer
from datetime import datetime
from writer import Writer
from utils import KUMULATIV_QUERIES, KUMULATIV_SHEET, KUMULATIV_TABLE_NAMES, DIESER_MONAT_QUERIES, DIESER_MONAT_SHEET, DIESER_MONAT_TABLE_NAMES, RISIKOKENNZAHLEN_VOLA_QUERIES, RISIKOKENNZAHLEN_VOLA_SHEET, RISIKOKENNZAHLEN_VOLA_TABLE_NAMES

load_dotenv()

db = mysql.connect(
  host=os.getenv('HOST'),
  user=os.getenv('USERNAME'),
  password=os.getenv('PASSWORD'),
  database=os.getenv('DATABASE')
)
print("Connected to:", db.get_server_info())

cursor = db.cursor()
today = datetime.today().date
# Create Pandas Excel writer using XlsxWriter engine
pandas_writer = pd.ExcelWriter('daten_{}.xlsx'.format(today), engine='xlsxwriter', options={'strings_to_numbers': True})
# Create custom Writer class
excel_writer = Writer(cursor, pandas_writer)

current_row = 1
query_index = 0
for query in KUMULATIV_QUERIES:
    last_row = excel_writer.write(current_row, query, query_index, 'Valor', KUMULATIV_SHEET, KUMULATIV_TABLE_NAMES)
    current_row = last_row + 6
    query_index += 1
current_row = 1
query_index = 0
for query in DIESER_MONAT_QUERIES:
    last_row = excel_writer.write(current_row, query, query_index, 'Valor', DIESER_MONAT_SHEET, DIESER_MONAT_TABLE_NAMES)
    current_row = last_row + 6
    query_index += 1
for query in RISIKOKENNZAHLEN_VOLA_QUERIES:
    last_row = excel_writer.write_with_plot(current_row, query, query_index, 'Wert', RISIKOKENNZAHLEN_VOLA_SHEET, RISIKOKENNZAHLEN_VOLA_TABLE_NAMES)
    current_row = last_row + 6
    query_index += 1

# Close the writer
pandas_writer.save()
