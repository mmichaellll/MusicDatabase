def read_csv_to_mysql():
    import csv
    import sqlite3

    #####================YOU NEED TO SET THESE VARIABLES VERY        CAREFULLY!!!!!==========
    #####================YOU NEED TO SET THESE VARIABLES VERY CAREFULLY!!!!!==========
    database_name = "music.db"
    table_name = "music"
    csv_filename = "musicmeww.csv"

    number_of_fields = 10  # set the number of fields - must be integer

    # Field names and their types to be used in database
    f1 = "ArtistFamiliarity"
    f1_type = "real"
    f2 = "ArtistHotttnesss"
    f2_type = "real"
    f3 = "ArtistID"
    f3_type = "text"
    f4 = "ArtistLatitude"
    f4_type = "real"
    f5 = "ArtistLocation"
    f5_type = "int"
    f6 = "ArtistLongitude"
    f6_type = "text"
    f7 = "ArtistName"
    f7_type = "text"
    f8 = "ArtistSimilar"
    f8_type = "real"
    f9 = "ArtistTerms"
    f9_type = "real"
    f10 = "SongYear"
    f10_type = "int"

    # YOU NEED TO ENSURE ALL FIELDNAME VARIABLES AND TYPES ARE INCLUDED IN THE ARGUMENT LIST BELOW
    SQL_create_table = f"CREATE TABLE {table_name} ({f1} {f1_type}, {f2} {f2_type}, {f3} {f3_type}, {f4} {f4_type}, {f5} {f5_type}, {f6} {f6_type}, {f7} {f7_type}, {f8} {f8_type}, {f9} {f9_type}, {f10} {f10_type})"

    # DON'T CHANGE THIS NEXT LINE
    SQL_place_holder_qmarks = "?" + (number_of_fields - 1) * ", ?"

    # YOU NEED TO ENSURE ALL FIELDNAME VARIABLES AND TYPES ARE INCLUDED IN THE ARGUMENT LIST BELOW
    SQL_insert_records = f"INSERT INTO {table_name} ({f1}, {f2}, {f3}, {f4}, {f5}, {f6}, {f7}, {f8},{f9},{f10}) VALUES({SQL_place_holder_qmarks})"

    #####====================DON'T TOUCH THE CODE BELOW HERE!!!!!==============
    #####====================DON'T TOUCH THE CODE BELOW HERE!!!!!==============

    ###===CREATE THE ACTUAL SQL QUERIES (DEPENDANT ON VARIABLES ABOVE) DON'T EDIT ANYTHING BELOW HERE
    SQL_check_table_is_clear = f"DROP TABLE IF EXISTS {table_name}"

    ###===THE CODE THAT ACTUALLY MAKES THE SQL DATABASE
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute(SQL_check_table_is_clear)
    cursor.execute(SQL_create_table)
    file = open(csv_filename, encoding="utf-8")
    contents = csv.reader(file)
    cursor.executemany(SQL_insert_records, contents)

    ###THIS CAN BE DELETED WHEN YOU KNOW YOUR FUNCTION WORKS
    ###===RUN A SAMPLE QUERY AND OUTPUT RESULTS
    # Output to the console screen

    # Committing the changes
    connection.commit()
    # closing the database connection
    connection.close()
