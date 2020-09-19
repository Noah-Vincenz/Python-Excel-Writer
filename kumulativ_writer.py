import pandas as pd

KUMULATIV_SHEET = 'kumulativ'

table_names = [
    "Abfrage kumulativ 1 Monat",
    "Abfrage kumulativ 3 Monate",
    "Abfrage kumulativ 6 Monate",
    "Abfrage kumulativ 1 Jahr",
    "Abfrage kumulativ 2 Jahre",
    "Abfrage kumulativ 3 Jahre",
    "Abfrage kumulativ 5 Jahre",
    "Abfrage kumulativ 10 Jahre"
]

def query(interval):
    return "SELECT datum, valor FROM `user_aktkurse_kurse` WHERE (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 0 year)) AND datum > '2008-12-01') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval {})) AND datum > '2008-12-01') ORDER BY datum ASC".format(interval)

queries = [
    query("1 month"),
    query("3 month"),
    query("6 month"),
    query("1 year"),
    query("2 year"),
    query("3 year"),
    query("5 year"),
    query("10 year")
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
        df.to_excel(writer, sheet_name=KUMULATIV_SHEET, startrow=rows)
        # Add table title
        worksheet = writer.sheets[KUMULATIV_SHEET]
        worksheet.write_string(rows - 1, 0, table_names[query_index])
        # Adding 5 rows spacing between tables
        rows = rows + len(data) + 7
        query_index += 1

