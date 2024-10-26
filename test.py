import sqlite_lib
import sql_query


def test_euro_winners_count():
    # Arrange
    sqlite_lib.connect('eur.db')

    # Act
    result = sqlite_lib.run_query_select('''
        SELECT COUNT(*) FROM eurovision_winners ew
    ''')

    # Assert
    assert result == [(68,)]


def test_song_details_count():
    sqlite_lib.connect('eur.db')

    result = sqlite_lib.run_query_select('''
        SELECT COUNT(*) FROM song_details s
    ''')

    assert result == [(68,)]


def country_year_true():
    sqlite_lib.connect('eur.db')

    result = sql_query.country_year(country='Israel', year=2018)

    assert result == [(2018, 'Israel', 'Netta', 'Portugal', 'Toy')]


def country_year_wrong():
    sqlite_lib.connect('eur.db')

    result = sql_query.country_year(country='Israel', year=2016)

    assert result == "invalid country or year"


def country_year_py_true():
    sqlite_lib.connect('eur.db')

    result = sql_query.country_year(country='Israel', year=2018)

    assert result == "invalid country or year"


def country_year_py_wrong():
    sqlite_lib.connect('eur.db')

    result = sql_query.country_year_python(country='Israel', year=2016)

    assert result == "invalid country or year"
