import mysql.connector as mysql
import os
import pandas as pd
from dotenv import load_dotenv
from writer import Writer
from utils import KUMULATIV_QUERIES, KUMULATIV_SHEET, KUMULATIV_TABLE_NAMES, RISIKOKENNZAHLEN_VOLA_QUERIES, RISIKOKENNZAHLEN_VOLA_SHEET, RISIKOKENNZAHLEN_VOLA_TABLE_NAMES, VALOR_QUERIES, VALOR_SHEET, VALOR_TABLE_NAMES, HISTORISCHE_WERTENTWICKLUNG_QUERIES, HISTORISCHE_WERTENTWICKLUNG_SHEET, HISTORISCHE_WERTENTWICKLUNG_TABLE_NAMES
from openpyxl import load_workbook

load_dotenv()

db = mysql.connect(
  host=os.getenv('HOST'),
  user=os.getenv('DB_USERNAME'),
  password=os.getenv('DB_PASSWORD'),
  database=os.getenv('DATABASE')
)
cursor = db.cursor()
#Create Pandas Excel writer using XlsxWriter engine
path = 'valor.xlsx'
book = load_workbook(filename = path)
pandas_writer = pd.ExcelWriter(path, engine = 'openpyxl', options = {'strings_to_numbers': True})
pandas_writer.book = book
#Create custom Writer class
excel_writer = Writer(book, cursor, pandas_writer)

#KUMULATIV
excel_writer.execute_queries(2, KUMULATIV_QUERIES, ['Datum', 'Summe von valor'], KUMULATIV_SHEET, KUMULATIV_TABLE_NAMES)
#RISIKOKENNZAHLEN VOLA
excel_writer.execute_queries(11, RISIKOKENNZAHLEN_VOLA_QUERIES, ['Datum', 'Wert'], RISIKOKENNZAHLEN_VOLA_SHEET, RISIKOKENNZAHLEN_VOLA_TABLE_NAMES)
#VALOR
excel_writer.execute_queries(2, VALOR_QUERIES, ['Datum', 'Summe von valor'], VALOR_SHEET, VALOR_TABLE_NAMES)
#HISTORISCHE WERTENTWICKLUNG
excel_writer.execute_queries(2, HISTORISCHE_WERTENTWICKLUNG_QUERIES, ['Datum', 'Valor'], HISTORISCHE_WERTENTWICKLUNG_SHEET, HISTORISCHE_WERTENTWICKLUNG_TABLE_NAMES)
#Close the writer
pandas_writer.save()
pandas_writer.close()
