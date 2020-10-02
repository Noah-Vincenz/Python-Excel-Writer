def generate_kumulativ_query(interval):
    return "SELECT datum, valor FROM `user_aktkurse_kurse` WHERE (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 0 year)) AND datum > '2008-12-01') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval {})) AND datum > '2008-12-01') ORDER BY datum ASC".format(interval)

# TODO: update this query to use similar style as for historische wertentwicklung
def generate_risikokennzahlen_vola_query(aktie):
    return '''SELECT datum, {}
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
KUMULATIV_SHEET = "kumulative_ertraege"
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
RISIKOKENNZAHLEN_VOLA_SHEET = "risikokennzahlen"
RISIKOKENNZAHLEN_VOLA_TABLE_NAMES = [
    "Abfrage Risikokennzahlen Vola CRB",
    "Abfrage Risikokennzahlen Vola Euribor",
    "Abfrage Risikokennzahlen Vola Valor"
]
VALOR_QUERIES = [
    "SELECT datum, valor FROM `user_aktkurse_kurse` WHERE (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 0 year)) AND datum > '2008-11-15') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 1 year)) AND datum > '2008-11-15') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 2 year)) AND datum > '2008-11-15') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 3 year)) AND datum > '2008-11-15') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 4 year)) AND datum > '2008-11-15') OR (datum = LAST_DAY(date_sub(LAST_DAY(date_sub(now(),interval 1 month)),interval 5 year)) AND datum > '2008-11-15') ORDER BY datum ASC"
]
VALOR_SHEET = "valor"
VALOR_TABLE_NAMES = ["Abfrage Valor"]
# "SELECT user_aktkurse_kurse_0.datum as Datum, user_aktkurse_kurse_0.valor FROM maisondo_kurse.user_aktkurse_kurse user_aktkurse_kurse_0"
# "SELECT user_aktkurse_kurse_0.datum as datum, user_aktkurse_kurse_0.valor FROM maisondo_kurse.user_aktkurse_kurse user_aktkurse_kurse_0 WHERE datum = LAST_DAY(datum)"
HISTORISCHE_WERTENTWICKLUNG_QUERIES = [
    '''SELECT user_aktkurse_kurse_0.datum as datum, user_aktkurse_kurse_0.valor 
    FROM maisondo_kurse.user_aktkurse_kurse user_aktkurse_kurse_0
    WHERE datum in 
    (SELECT DISTINCT MAX(datum) FROM maisondo_kurse.user_aktkurse_kurse user_aktkurse_kurse_0 GROUP BY MONTH(datum))
    AND datum >= DATE_SUB(now(), INTERVAL 5 YEAR)
    ORDER BY datum ASC'''
]
HISTORISCHE_WERTENTWICKLUNG_SHEET = "historische_wertentwicklung"
HISTORISCHE_WERTENTWICKLUNG_TABLE_NAMES = ["Abfrage von historische Wertentwicklung 5 Jahre"] # add 10 Jahre Query
