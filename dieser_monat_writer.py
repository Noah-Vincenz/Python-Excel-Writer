import pandas as pd

DIESER_MONAT_SHEET = 'dieser_monat'

table_names = [
    "Abfrage dieser Monat"
]

queries = [
    "SELECT datum, valor FROM `user_aktkurse_kurse` WHERE (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 0 year)) AND datum > '2008-12-01') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 1 month)) AND datum > '2008-12-01') ORDER BY datum ASC"
]

def write(cursor, writer):
    rows = 1
    query_index = 0
    for query in queries:
        cursor.execute(query)
        data = cursor.fetchall()
        # Create Pandas dataframe from the data
        df = pd.DataFrame(data, columns=['Datum', 'Valor'])
        # Convert dataframe to XlsxWriter Excel object
        df.to_excel(writer, sheet_name=DIESER_MONAT_SHEET, startrow=rows)
        # Add table title
        worksheet = writer.sheets[DIESER_MONAT_SHEET]
        worksheet.write_string(rows - 1, 0, table_names[query_index])
        # Adding 5 rows spacing between tables
        rows = rows + len(data) + 7
        query_index += 1

