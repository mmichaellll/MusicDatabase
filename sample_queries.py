# Sample queries that you might be able to adapt and use:

import sqlite3
import tkinter as tk
import tkinter.simpledialog

def find_records_with_user_entered_criteria():

    database_name = "music.db"
    table_name = "music"

    # get user input using tkinter input dialog
    root = tk.Tk()
    root.withdraw()
    user_in = tk.simpledialog.askstring(
        title="Find Records with User-Entered Criteria", prompt="Name an artist:"
    )

    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    SQL_query = f"SELECT ArtistFamiliarity, ArtistHotttnesss, ArtistName, ArtistTerms, SongYear FROM {table_name} WHERE ArtistName = '{user_in}'"
    rows = cursor.execute(SQL_query).fetchall()

    results_window = tk.Toplevel(root)
    results_window.geometry("500x500")

    # create a Text widget to display the results
    results_text = tk.Text(results_window)
    results_text.pack(expand=True, fill="both")

    # add headings to the Text widget
    results_text.insert(
        tk.END,
        f"{'Artist Familiarity':<25} {'Artist Popularity':<25} {'Artist Name':<25} {'Artist Genre':<25} {'Song Year':<10}\n",
    )
    results_text.insert(tk.END, "-" * 115 + "\n")

    # add each row to the Text widget
    for r in rows:
        results_text.insert(
            tk.END, f"{r[0]:<25} {r[1]:<25} {r[2]:<25} {r[3]:<25} {r[4]:<10}\n"
        )

    connection.close()


def add_a_record():


    database_name = "music.db"
    table_name = "music"

    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    familiarity = tk.simpledialog.askstring(
        title="Add a record", prompt="Artist Familiarity:"
    )
    hotness = tk.simpledialog.askstring(
        title="Add a record", prompt="Artist Hotttnesss:"
    )
    idd = tk.simpledialog.askstring(title="Add a record", prompt="Artist ID:")
    lat = tk.simpledialog.askstring(title="Add a record", prompt="Artist Latitude:")
    location = tk.simpledialog.askstring(
        title="Add a record", prompt="Artist Location:"
    )
    long = tk.simpledialog.askstring(title="Add a record", prompt="Artist Longitude:")
    name = tk.simpledialog.askstring(title="Add a record", prompt="Artist Name:")
    similar = tk.simpledialog.askstring(title="Add a record", prompt="Artist Similar:")
    genre = tk.simpledialog.askstring(title="Add a record", prompt="Artist Genre:")
    year = tk.simpledialog.askstring(title="Add a record", prompt="Song Year:")
    # Add some records to the table
    cursor.execute(
        f"INSERT INTO {table_name} (ArtistFamiliarity, ArtistHotttnesss, ArtistID, ArtistLatitude, ArtistLocation, ArtistLongitude, ArtistName, ArtistSimilar, ArtistTerms, SongYear) VALUES('{familiarity}', '{hotness}', '{idd}', '{lat}', '{location}', '{long}', '{name}', '{similar}', '{genre}','{year}');"
    )

    # Committing the changes
    connection.commit()
    # closing the database connection
    connection.close()

    root = tk.Tk()
    root.withdraw()
    results_window = tk.Toplevel(root)
    results_window.geometry("500x500")
    results_text = tk.Text(results_window)
    results_text.pack(expand=True, fill="both")
    results_text.insert(tk.END, "Added Data Entry!")


def search_through_DB_for_criteria():
    database_name = "music.db"
    table_name = "music"

    criteria = tk.simpledialog.askstring(
        title="Search for Criteria",
        prompt="What Field do you want to search in? (ArtistFamiliarity, ArtistHotttnesss, ArtistID. ArtistLatitude, ArtistLocation, ArtistLongitude, ArtistName, ArtistSimilar, ArtistTerms, SongYear)",
    )
    entry = tk.simpledialog.askstring(
        title="Search for Criteria", prompt="What value do you want to look for?"
    )
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    SQL_query = f"SELECT * FROM {table_name} WHERE {criteria} = '{entry}'"

    rows = cursor.execute(SQL_query).fetchall()

    root = tk.Tk()
    results_window = tk.Toplevel(root)
    results_window.geometry("500x500")

    # create a Text widget to display the results
    results_text = tk.Text(results_window)
    results_text.pack(expand=True, fill="both")

    # add headings to the Text widget
    results_text.insert(
        tk.END,
        f"{'ArtistFamiliarity':<25} {'ArtistHotttnesss':<25} {'ArtistID':<25} {'ArtistLatitude':<25} {'ArtistLocation':<25}{'ArtistLongitude':<25}{'ArtistName':<25}{'ArtistSimilar':<25}{'ArtistTerms':<25}{'SongYear':<10}\n",
    )
    results_text.insert(tk.END, "-" * 115 + "\n")

    # add each row to the Text widget
    for r in rows:
        results_text.insert(
            tk.END,
            f"{r[0]:<25} {r[1]:<25} {r[2]:<25} {r[3]:<25} {r[4]:<25}{r[5]:<25}{r[6]:<25}{r[7]:<25}{r[8]:<25}{r[9]:<10}\n",
        )

    connection.close()


def delete_fields():

    database_name = "music.db"
    table_name = "music"

    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    field = tk.simpledialog.askstring(
        title="Delete a Record", prompt="What Field do you want to search in? (ArtistFamiliarity, ArtistHotttnesss, ArtistID. ArtistLatitude, ArtistLocation, ArtistLongitude, ArtistName, ArtistSimilar, ArtistTerms, SongYear)"
    )
    value = tk.simpledialog.askstring(
        title="Delete a Record", prompt="Which value do you want to delete?"
    )

    # Add some records to the table
    cursor.execute(
        f"DELETE FROM {table_name} WHERE {field} = '{value}';"
    )

    # Committing the changes
    connection.commit()
    # closing the database connection
    connection.close()

    root = tk.Tk()
    root.withdraw()
    results_window = tk.Toplevel(root)
    results_window.geometry("500x500")
    results_text = tk.Text(results_window)
    results_text.pack(expand=True, fill="both")
    results_text.insert(tk.END, "Removed Data Entry!")
def sort_db():

    database_name = "music.db"
    table_name = "music"

    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    fieldname = tk.simpledialog.askstring(
        title="Sort the DB", prompt="What Field do you want to sort in? (ArtistFamiliarity, ArtistHotttnesss, ArtistID. ArtistLatitude, ArtistLocation, ArtistLongitude, ArtistName, ArtistSimilar, ArtistTerms, SongYear)"
    )
    ASCORDEC = tk.simpledialog.askstring(
        title="Sort the DB", prompt="ASC or DESC?"
    )

    SQL_query = f"SELECT * FROM {table_name} ORDER BY {fieldname} {ASCORDEC}"

    rows = cursor.execute(SQL_query).fetchall()

    root = tk.Tk()
    root.withdraw()
    results_window = tk.Toplevel(root)
    results_window.geometry("500x500")

    # create a Text widget to display the results
    results_text = tk.Text(results_window)
    results_text.pack(expand=True, fill="both")

    # add headings to the Text widget
    results_text.insert(
        tk.END,
        f"{'ArtistFamiliarity':<25} {'ArtistHotttnesss':<25} {'ArtistID':<25} {'ArtistLatitude':<25} {'ArtistLocation':<25}{'ArtistLongitude':<25}{'ArtistName':<25}{'ArtistSimilar':<25}{'ArtistTerms':<25}{'SongYear':<10}\n",
    )
    results_text.insert(tk.END, "-" * 194 + "\n")

    # add each row to the Text widget
    for r in rows:
        results_text.insert(
            tk.END,
            f"{r[0]:<25} {r[1]:<25} {r[2]:<25} {r[3]:<25} {r[4]:<25}{r[5]:<25}{r[6]:<25}{r[7]:<25}{r[8]:<25}{r[9]:<10}\n",
        )

    connection.close()

def print_db():


    database_name = "music.db"
    table_name = "music"

    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    SQL_query = f"SELECT * FROM {table_name}"

    rows = cursor.execute(SQL_query).fetchall()

    root = tk.Tk()
    root.withdraw()
    results_window = tk.Toplevel(root)
    results_window.geometry("500x500")

    # create a Text widget to display the results
    results_text = tk.Text(results_window)
    results_text.pack(expand=True, fill="both")

    # add headings to the Text widget
    results_text.insert(
        tk.END,
        f"{'ArtistFamiliarity':<25} {'ArtistHotttnesss':<25} {'ArtistID':<25} {'ArtistLatitude':<25} {'ArtistLocation':<25}{'ArtistLongitude':<25}{'ArtistName':<25}{'ArtistSimilar':<25}{'ArtistTerms':<25}{'SongYear':<10}\n",
    )
    results_text.insert(tk.END, "-" * 194 + "\n")

    # add each row to the Text widget
    for r in rows:
        results_text.insert(
            tk.END,
            f"{r[0]:<25} {r[1]:<25} {r[2]:<25} {r[3]:<25} {r[4]:<25}{r[5]:<25}{r[6]:<25}{r[7]:<25}{r[8]:<25}{r[9]:<10}\n",
        )

    connection.close()

def update_records():
    """Update a record in the database."""
    database_name = "music.db"
    table_name = "music"

    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    artist_name = tk.simpledialog.askstring(
        title="Update a Record", prompt="Enter the name of the artist you want to update:"
    )

    new_familiarity = tk.simpledialog.askstring(
        title="Update a Record", prompt="Enter the new value for Artist Familiarity:"
    )
    new_hotness = tk.simpledialog.askstring(
        title="Update a Record", prompt="Enter the new value for Artist Hotttnesss:"
    )
    new_genre = tk.simpledialog.askstring(
        title="Update a Record", prompt="Enter the new value for Artist Genre:"
    )
    new_year = tk.simpledialog.askstring(
        title="Update a Record", prompt="Enter the new value for Song Year:"
    )

    # Update the record in the table
    cursor.execute(
        f"UPDATE {table_name} SET ArtistFamiliarity='{new_familiarity}', ArtistHotttnesss='{new_hotness}', ArtistTerms='{new_genre}', SongYear='{new_year}' WHERE ArtistName='{artist_name}'"
    )

    # Committing the changes
    connection.commit()
    # closing the database connection
    connection.close()
