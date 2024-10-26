import sqlite_lib


def years_10():
    # Connect to the database
    sqlite_lib.connect('eur.db')

    # Run the query to fetch the last 10 Eurovision winners ordered by year
    result = sqlite_lib.run_query_select('''
    SELECT * FROM eurovision_winners
    ORDER BY year DESC
    LIMIT 10
    ''')

    # Print the result
    for row in result:
        year, country, winner, host_country, song_name = row
        print(f'{year:<6} {country:<15} {winner:<30} {host_country:<15} {song_name:<30}')

    # Close the connection
    sqlite_lib.close()


def country_year():
    sqlite_lib.connect('eur.db')
    while True:
        country = input("enter a country").strip()
        year = input("enter a year").strip()
        result = sqlite_lib.run_query_select('''
        SELECT * FROM eurovision_winners
        WHERE country = ? AND year = ?
        ''', (country, year))

        if result:
            print(result)
            break
        else:
            print(f"No results found for {country, year}, try another country or year")
            continue
    sqlite_lib.close()


def country_year_python():
    data = sqlite_lib.run_query_select("SELECT * FROM eurovision_winners")
    while True:
        country = input("enter country").strip()
        year = input("enter year")

        try:
            year = int(year)
        except ValueError:
            print("Year must be a number. Try again.")
            continue

        result = list(filter(lambda x: (x[0] == year and x[1] == country), data))
        if result:
            for entry in result:
                print(entry)
            return result  # Returning for potential test verification
        else:
            print("Invalid country or year. Try again.")


def change_genre():
    sqlite_lib.connect('eur.db')

    while True:
        country = input("enter country: ").strip()
        year = input("enter year: ").strip()
        genre = input("change genre to: ").strip()

        # Verify song exists by joining the tables
        result = sqlite_lib.run_query_select('''
            SELECT s.year, s.genre, eu.country FROM song_details s
            JOIN eurovision_winners eu ON s.year = eu.year
            WHERE s.year = ? AND eu.country = ?
        ''', (year, country))

        if result:
            for row in result:
                year, current_genre, country = row
                fff = country_year_python()  # Call without args for inputs within function

                if fff:
                    if current_genre is None or current_genre.strip() == "":
                        print(f"No existing genre found for the song in {country} ({year}).")
                        print(f"Setting genre to '{genre}' as the new genre.")
                    elif genre == current_genre:
                        print("Genre is the same as the current genre. Please enter a different genre.")
                        break

                    # Update query focusing only on year for song_details
                    sqlite_lib.run_query_update('''
                        UPDATE song_details
                        SET genre = ?
                        WHERE year = ?
                    ''', (genre, year))
                    print(f"Genre changed to '{genre}' for the song in {country} ({year}).")
                    sqlite_lib.close()
                    return
        else:
            print(f"No song found for country '{country}' and year '{year}'. Please try again.")


if __name__ == "__main__":
    # years_10()
    # country_year(None, None)
    # country_year_python(None, None)
    change_genre()