import pandas as pd

FONT = {'size': 14, 'bold': True}

class Writer:

    def __init__(self, cursor, writer):
        self.cursor = cursor
        self.writer = writer

    def execute_queries(self, queries, columns, sheet_name, table_names):
        current_row = 1
        query_index = 0
        for query in queries:
            last_row = self.write(current_row, query, query_index, columns, sheet_name, table_names)
            current_row = last_row + 6
            query_index += 1

    def execute_queries_with_plot(self, queries, columns, sheet_name, table_names):
        current_row = 1
        query_index = 0
        for query in queries:
            last_row = self.write_with_plot(current_row, query, query_index, columns, sheet_name, table_names)
            current_row = last_row + 6
            query_index += 1

    def write(self, current_row, query, query_index, columns, sheet_name, table_names):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        last_row = current_row + len(data) + 1
        # Create Pandas dataframe from the data
        df = pd.DataFrame(data, columns=columns)
        # Convert dataframe to XlsxWriter Excel object
        df.to_excel(self.writer, sheet_name=sheet_name, startrow=current_row)
        worksheet = self.writer.sheets[sheet_name]
        # Increase column width for date
        if columns[0] == 'Datum':
            worksheet.set_column(1, 1, 10)
        # Add table title
        worksheet.write_string(current_row - 1, 0, table_names[query_index])
        return last_row

    def write_with_plot(self, current_row, query, query_index, columns, sheet_name, table_names):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        first_row = current_row + 2
        last_row = current_row + len(data) + 1
        # Create Pandas dataframe from the data
        df = pd.DataFrame(data, columns=columns)
        min_value = df[columns[0]].min()
        # Convert dataframe to XlsxWriter Excel object
        df.to_excel(self.writer, sheet_name=sheet_name, startrow=current_row)
        worksheet = self.writer.sheets[sheet_name]
        # Increase column width for date
        if columns[0] == 'Datum':
            worksheet.set_column(1, 1, 10)
        # Add table title
        worksheet.write_string(current_row - 1, 0, table_names[query_index])
        # Add colouring to values
        worksheet.conditional_format('C{}:C{}'.format(first_row, last_row), {'type': '3_color_scale'})
        self.create_chart(worksheet, data, query_index, columns[0], min_value, first_row, last_row, sheet_name, table_names)
        return last_row


    def create_chart(self, worksheet, data, query_index, column, min_value, first_row, last_row, sheet_name, table_names):
        # Create a chart object
        workbook  = self.writer.book
        chart = workbook.add_chart({'type': 'line'})
        chart.set_size({'width': 900, 'height': 550})
        chart.set_y_axis({
            'name': column,
            'name_font': FONT
        })
        chart.set_x_axis({
            'name': 'Datum',
            'name_font': FONT
        })
        chart.set_title({ 'name': table_names[query_index]})
        chart.set_legend({'none': True})
        chart.set_style(37)
        # Configure the series of the chart from the data
        y_values = '={}!$C${}:$C${}'.format(sheet_name, first_row, last_row)
        x_values = '={}!$B${}:$B${}'.format(sheet_name, first_row, last_row)
        chart.add_series({'name': column, 'values': y_values, 'categories': x_values})

        # Insert the chart into the worksheet.
        worksheet.insert_chart('F{}'.format(first_row), chart)