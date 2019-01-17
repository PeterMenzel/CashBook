import sqlite3
from tkinter import *
from tkinter import ttk

ACCOUNTS = ['ANZ - Visa', 'ANZ - Debit', 'Bendigo']
YEARS = ['2014', '2015', '2016', '2017', '2018', '2019']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

root = Tk()
root.state('zoomed')
root.title("Cash Book")

main_frame = Frame(root, background="white")
main_frame.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+W+E)
# main_frame.grid_columnconfigure(0, weight=1)

selection_frame = LabelFrame(main_frame)
selection_frame.grid(row=0, column=0, sticky=W)

account_combobox = ttk.Combobox(selection_frame, state="readonly")
# account_combobox['values'] = ('ANZ - Visa', 'ANZ - Debit', 'Bendigo')
account_combobox['values'] = ACCOUNTS
account_combobox.grid(row=0, column=0, sticky=W)

year_combobox = ttk.Combobox(selection_frame, state="readonly")
year_combobox['values'] = YEARS
year_combobox.grid(row=0, column=1, sticky=W)

month_combobox = ttk.Combobox(selection_frame)
month_combobox['values'] = MONTHS
month_combobox['state'] = "readonly"
month_combobox.grid(row=0, column=2, sticky=W)

add_account = Button(main_frame, text="Add Bank")
add_account.grid(row=0, column=3, sticky=E)

# Create multiple LabelFrames

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)

# Button(main_frame, text="Submit").grid(row=3)

root.mainloop()
