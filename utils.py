def generate_kumulativ_query(interval):
    return "SELECT datum, valor FROM `user_aktkurse_kurse` WHERE (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 0 year)) AND datum > '2008-12-01') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval {})) AND datum > '2008-12-01') ORDER BY datum ASC".format(interval)

def generate_risikokennzahlen_vola_query(aktie):
    return '''
    SELECT datum, {} 
    FROM `user_aktkurse_kurse` 
    WHERE datum = LAST_DAY(datum) AND datum > DATE_SUB(now(), INTERVAL 37 MONTH)
    ORDER BY datum ASC
    '''.format(aktie)

KUMULATIV_QUERIES = [
    "SELECT datum, valor FROM `user_aktkurse_kurse` WHERE (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 0 year)) AND datum > '2008-12-01') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 1 month)) AND datum > '2008-12-01') ORDER BY datum ASC",
    generate_kumulativ_query("1 month"),
    generate_kumulativ_query("3 month"),
    generate_kumulativ_query("6 month"),
    generate_kumulativ_query("1 year"),
    generate_kumulativ_query("2 year"),
    generate_kumulativ_query("3 year"),
    generate_kumulativ_query("5 year"),
    generate_kumulativ_query("10 year")
]
KUMULATIV_SHEET = "kumulative Ertraege"
KUMULATIV_TABLE_NAMES = [
    "Dieser Monat",
    "1 Monat",
    "3 Monate",
    "6 Monate",
    "1 Jahr",
    "2 Jahre",
    "3 Jahre",
    "5 Jahre",
    "10 Jahre"
]
RISIKOKENNZAHLEN_VOLA_QUERIES = [
    generate_risikokennzahlen_vola_query("CRB"),
    generate_risikokennzahlen_vola_query("Euribor3m"),
    generate_risikokennzahlen_vola_query("Valor")
]
RISIKOKENNZAHLEN_VOLA_SHEET = "Risikokennzahlen"
RISIKOKENNZAHLEN_VOLA_TABLE_NAMES = [
    "Abfrage Risikokennzahlen Vola CRB",
    "Abfrage Risikokennzahlen Vola Euribor",
    "Abfrage Risikokennzahlen Vola Valor"
]
VALOR_QUERIES = [
    "SELECT datum, valor FROM `user_aktkurse_kurse` WHERE (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 0 year)) AND datum > '2008-11-15') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 1 year)) AND datum > '2008-11-15') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 2 year)) AND datum > '2008-11-15') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 3 year)) AND datum > '2008-11-15') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 4 year)) AND datum > '2008-11-15') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 5 year)) AND datum > '2008-11-15') ORDER BY datum ASC"
]
VALOR_SHEET = "Valor"
VALOR_TABLE_NAMES = ["Abfrage Valor"]
HISTORISCHE_WERTENTWICKLUNG_QUERIES = [
    '''
    SELECT user_aktkurse_kurse_0.datum as datum, user_aktkurse_kurse_0.valor 
    FROM maisondo_kurse.user_aktkurse_kurse user_aktkurse_kurse_0 
    WHERE datum = LAST_DAY(datum) AND datum > DATE_SUB(now(), INTERVAL 61 MONTH)
    ORDER BY datum ASC
    ''',
    '''
    SELECT user_aktkurse_kurse_0.datum as datum, user_aktkurse_kurse_0.valor 
    FROM maisondo_kurse.user_aktkurse_kurse user_aktkurse_kurse_0 
    WHERE datum = LAST_DAY(datum) AND datum > DATE_SUB(now(), INTERVAL 121 MONTH)
    ORDER BY datum ASC
    '''
]
HISTORISCHE_WERTENTWICKLUNG_SHEET = "historische Wertentwicklung"
HISTORISCHE_WERTENTWICKLUNG_TABLE_NAMES = ["Abfrage von historische Wertentwicklung 5 Jahre", "Abfrage von historische Wertentwicklung 10 Jahre"]
