import pandas as pd

class Writer:

    def __init__(self, cursor, writer):
        self.cursor = cursor
        self.writer = writer

    def write(self, current_row, query, query_index, values_column, sheet_name, table_names):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        last_row = current_row + len(data) + 1
        # Create Pandas dataframe from the data
        df = pd.DataFrame(data, columns=['Datum', values_column])
        # Convert dataframe to XlsxWriter Excel object
        df.to_excel(self.writer, sheet_name=sheet_name, startrow=current_row)
        worksheet = self.writer.sheets[sheet_name]
        # Increase column width for date
        worksheet.set_column(1, 1, 12)
        # Add table title
        worksheet.write_string(current_row - 1, 0, table_names[query_index])
        return last_row

    def write_with_plot(self, current_row, query, query_index, values_column, sheet_name, table_names):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        first_row = current_row + 2
        last_row = current_row + len(data) + 1
        # Create Pandas dataframe from the data
        df = pd.DataFrame(data, columns=['Datum', values_column])
        # Convert dataframe to XlsxWriter Excel object
        df.to_excel(self.writer, sheet_name=sheet_name, startrow=current_row)
        worksheet = self.writer.sheets[sheet_name]
        # Increase column width for date
        worksheet.set_column(1, 1, 12)
        # Add table title
        worksheet.write_string(current_row - 1, 0, table_names[query_index])
        # Add colouring to values
        worksheet.conditional_format('C{}:C{}'.format(first_row, last_row), {'type': '3_color_scale'})
        self.create_chart(worksheet, data, query_index, values_column, first_row, last_row, sheet_name, table_names)
        return last_row


    def create_chart(self, worksheet, data, query_index, values_column, first_row, last_row, sheet_name, table_names):
        # Create a chart object
        workbook  = self.writer.book
        chart = workbook.add_chart({'type': 'line'})
        chart.set_size({'width': len(data) * 25, 'height': 550})
        chart.set_y_axis({
            'min': 100, # TODO: populate dynamically by finding out min value - 20 from first row to last row
            'name': values_column,
            'name_font': {'size': 14, 'bold': True}
        })
        chart.set_x_axis({
            'name': 'Datum',
            'name_font': {'size': 14, 'bold': True}
        })
        chart.set_title({ 'name': table_names[query_index]})
        chart.set_legend({'none': True})
        chart.set_style(37) # check this
        # Configure the series of the chart from the dataframe data.
        y_values = '={}!$C${}:$C${}'.format(sheet_name, first_row, last_row)
        x_values = '={}!$B${}:$B${}'.format(sheet_name, first_row, last_row)
        chart.add_series({'name': values_column, 'values': y_values, 'categories': x_values})

        # Insert the chart into the worksheet.
        worksheet.insert_chart('F{}'.format(first_row), chart)