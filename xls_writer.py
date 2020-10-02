import mysql.connector as mysql
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime
from writer import Writer
from utils import KUMULATIV_QUERIES, KUMULATIV_SHEET, KUMULATIV_TABLE_NAMES, RISIKOKENNZAHLEN_VOLA_QUERIES, RISIKOKENNZAHLEN_VOLA_SHEET, RISIKOKENNZAHLEN_VOLA_TABLE_NAMES, VALOR_QUERIES, VALOR_SHEET, VALOR_TABLE_NAMES, HISTORISCHE_WERTENTWICKLUNG_QUERIES, HISTORISCHE_WERTENTWICKLUNG_SHEET, HISTORISCHE_WERTENTWICKLUNG_TABLE_NAMES

load_dotenv()

db = mysql.connect(
  host=os.getenv('HOST'),
  user=os.getenv('USERNAME'),
  password=os.getenv('PASSWORD'),
  database=os.getenv('DATABASE')
)
print("Connected to:", db.get_server_info())

cursor = db.cursor()
today = datetime.today().date()
#Create Pandas Excel writer using XlsxWriter engine
pandas_writer = pd.ExcelWriter('daten_{}.xlsx'.format(today), engine='xlsxwriter', options={'strings_to_numbers': True})
#Create custom Writer class
excel_writer = Writer(cursor, pandas_writer)

#KUMULATIV
excel_writer.execute_queries(KUMULATIV_QUERIES, ['Datum', 'Summe von valor'], KUMULATIV_SHEET, KUMULATIV_TABLE_NAMES)
#RISIKOKENNZAHLEN VOLA
excel_writer.execute_queries_with_plot(RISIKOKENNZAHLEN_VOLA_QUERIES, ['Datum', 'Wert'], RISIKOKENNZAHLEN_VOLA_SHEET, RISIKOKENNZAHLEN_VOLA_TABLE_NAMES)
#VALOR
excel_writer.execute_queries_with_plot(VALOR_QUERIES, ['Datum', 'Summe von valor'], VALOR_SHEET, VALOR_TABLE_NAMES)
#HISTORISCHE WERTENTWICKLUNG
excel_writer.execute_queries_with_plot(HISTORISCHE_WERTENTWICKLUNG_QUERIES, ['Datum', 'Valor'], HISTORISCHE_WERTENTWICKLUNG_SHEET, HISTORISCHE_WERTENTWICKLUNG_TABLE_NAMES)
#Close the writer
pandas_writer.save()
