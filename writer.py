import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows

class Writer:

    def __init__(self, book, cursor, writer):
        self.book = book
        self.cursor = cursor
        self.writer = writer

    def execute_queries(self, first_row, queries, columns, sheet_name, table_names):
        current_row = first_row
        query_index = 0
        for query in queries:
            last_row = self.write(current_row, query, query_index, columns, sheet_name, table_names)
            current_row = last_row + 6
            query_index += 1

    def write(self, first_row, query, query_index, columns, sheet_name, table_names):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        last_row = first_row + len(data) + 1
        # Create Pandas dataframe from the data
        df = pd.DataFrame(data, columns=columns)
        worksheet = self.book[sheet_name]
        df[columns[1]] = df[columns[1]].astype(float)
        current_row = first_row
        for r in dataframe_to_rows(df, index=False, header=True):
            worksheet.cell(row=current_row, column=1).value = r[0]
            worksheet.cell(row=current_row, column=2).value = r[1]
            current_row += 1
        # Add table title
        worksheet.cell(row=first_row - 1, column=1, value=table_names[query_index])
        # Add colouring to values
        # worksheet.conditional_format('B{}:B{}'.format(first_row, last_row), {'type': '3_color_scale'})
        return last_row
