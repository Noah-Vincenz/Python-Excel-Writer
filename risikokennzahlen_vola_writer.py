import pandas as pd

RISIKOKENNZAHLEN_VOLA_SHEET = 'risikokennzahlen_vola'

table_names = [
    "Abfrage Risikokennzahlen Vola CRB",
    "Abfrage Risikokennzahlen Vola Euribor"
]

queries = [
'''SELECT datum, CRB
FROM `user_aktkurse_kurse`
WHERE
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 0 year)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 1 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 2 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 3 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 4 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 5 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 6 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 7 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 8 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 9 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 10 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 11 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 12 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 13 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 14 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 15 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 16 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 17 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 18 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 19 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 20 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 21 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 22 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 23 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 24 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 25 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 26 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 27 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 28 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 29 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 30 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 31 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 32 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 33 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 34 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 35 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 36 month)) AND datum > '2008-12-01')
ORDER BY datum ASC
''',
'''
SELECT datum, Euribor3m
FROM `user_aktkurse_kurse`
WHERE
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 0 year)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 1 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 2 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 3 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 4 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 5 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 6 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 7 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 8 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 9 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 10 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 11 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 12 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 13 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 14 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 15 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 16 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 17 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 18 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 19 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 20 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 21 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 22 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 23 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 24 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 25 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 26 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 27 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 28 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 29 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 30 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 31 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 32 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 33 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 34 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 35 month)) AND datum > '2008-12-01')
OR
(datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 36 month)) AND datum > '2008-12-01')
ORDER BY datum ASC
'''
]

def write(cursor, writer):
    rows = 1
    query_index = 0
    for query in queries:
        cursor.execute(query)
        data = cursor.fetchall()
        # Create Pandas dataframe from the data
        df = pd.DataFrame(data, columns=['Datum', 'Wert'])
        # Convert dataframe to XlsxWriter Excel object
        df.to_excel(writer, sheet_name=RISIKOKENNZAHLEN_VOLA_SHEET, startrow=rows)
        worksheet = writer.sheets[RISIKOKENNZAHLEN_VOLA_SHEET]
        # Add table title
        worksheet.write_string(rows - 1, 0, table_names[query_index])
        # Apply a conditional format to the cell range.
        # Adds colouring to values
        worksheet.conditional_format('C3:C39', {'type': '3_color_scale'})
        # Create a chart object
        workbook  = writer.book
        chart = workbook.add_chart({'type': 'line'})
        chart.set_size({'width': 900, 'height': 576})
        chart.set_y_axis({
            'name': 'Wert',
            'name_font': {'size': 14, 'bold': True}
        })
        chart.set_x_axis({
            'name': 'Datum',
            'name_font': {'size': 14, 'bold': True}
        })
        chart.set_title({ 'name': table_names[query_index]})

        # Configure the series of the chart from the dataframe data.
        y_values = '={}!$C$3:$C$39'.format(RISIKOKENNZAHLEN_VOLA_SHEET)
        x_values = '={}!$B$3:$B$39'.format(RISIKOKENNZAHLEN_VOLA_SHEET)
        chart.add_series({'name': 'Wert', 'values': y_values, 'categories': x_values})

        # Insert the chart into the worksheet.
        worksheet.insert_chart('F3', chart)
        # Adding 5 rows spacing between tables
        rows = rows + len(data) + 7
        # Go to next query  
        query_index += 1

