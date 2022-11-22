SQL_COLS = {
    'staff': """id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                l_name TEXT NOT NULL,
                gender TEXT NOT NULL,
                department TEXT NOT NULL
                """,

    'info': """ id INTEGER PRIMARY KEY,
                position TEXT NOT NULL,
                birth_date TEXT NOT NULL,
                phone_num TEXT NOT NULL,
                city TEXT NOT NULL
                """
}
