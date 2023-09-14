"""import the necessary libraries"""
import sys
import tkinter as tk
from sample_queries import (
    add_a_record,
    delete_fields,
    find_records_with_user_entered_criteria,
    print_db,
    search_through_DB_for_criteria,
    sort_db,
    update_records,
)
from create_the_database import read_csv_to_mysql


read_csv_to_mysql()

# define the function to execute when the window is closed


def close_window():
    """Close the window and exit the program"""
    sys.exit()


# define the functions to execute when the buttons are clicked
def search_function():
    """Search for a record with user-entered criteria"""
    find_records_with_user_entered_criteria()


def add_function():
    """Add a record to the database"""
    add_a_record()


def search_for_criteria():
    """Search through fields for criteria"""
    search_through_DB_for_criteria()


def delete_value():
    """Delete a value from the database"""
    delete_fields()


def print_dbs():
    """Print the database"""
    print_db()


def sort_dbs():
    """Sort the database"""
    sort_db()
def update_record():
  update_records()
# create the GUI window
window = tk.Tk()

# set the window title
window.title("Database Management System")

# set the background and foreground colors
bg_color = "#E5F1F5"
# fg_color = "#000000"
window.config(bg=bg_color)

# set the color palette for the buttons
button_bg = "#FFFFFF"
button_fg = "#000000"
button_active_bg = "#8FB6D0"
button_active_fg = "#FFFFFF"

# center the window on the screen
window_width = 600
window_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coord = int((screen_width / 2) - (window_width / 2))
y_coord = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x_coord}+{y_coord}")

T = tk.Text(window, height=1, width=55)
T.pack()
T.insert(tk.END, "Hello! Just press on the buttons to use this program")
T.configure(state="disabled")

# create the button widgets and add them to the window
button1 = tk.Button(
 window,
 text="Search for Artist Name",
 command=search_function,
 bg=button_bg,
 fg=button_fg,
 activebackground=button_active_bg,
 activeforeground=button_active_fg,
 width=35,
)
button1.pack(pady=10)

button2 = tk.Button(
 window,
 text="Add a Record",
 command=add_function,
 bg=button_bg,
 fg=button_fg,
 activebackground=button_active_bg,
 activeforeground=button_active_fg,
 width=35,
)
button2.pack(pady=10)
button3 = tk.Button(
 window,
 text="Search through fields for Criteria",
 command=search_for_criteria,
 bg=button_bg,
 fg=button_fg,
 activebackground=button_active_bg,
 activeforeground=button_active_fg,
 width=35,
)
button3.pack(pady=10)
button4 = tk.Button(
 window,
 text="Delete Fields",
 command=delete_value,
 bg=button_bg,
 fg=button_fg,
 activebackground=button_active_bg,
 activeforeground=button_active_fg,
 width=35,
)
button4.pack(pady=10)
button5 = tk.Button(
 window,
 text="Print DB",
 command=print_dbs,
 bg=button_bg,
 fg=button_fg,
 activebackground=button_active_bg,
 activeforeground=button_active_fg,
 width=35,
)
button5.pack(pady=10)
button6 = tk.Button(
    window,
    text="Sort DB",
    command=sort_dbs,
    bg=button_bg,
    fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    width=35,
)
button6.pack(pady=10)

button7 = tk.Button(
    window,
    text="Update a Record",
    command=update_record,
    bg=button_bg,
    fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    width=35,
)
button7.pack(pady=10)

button8 = tk.Button(
    window,
    text="Exit",
    command=close_window,
    bg=button_bg,
    fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    width=35,
)
button8.pack(pady=10)

# run the GUI loop
window.mainloop()
