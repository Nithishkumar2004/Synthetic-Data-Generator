import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
import re

csv_file_path = 'rating_adjectives.csv'

def add_record():
    rating = rating_var.get()
    adjective = adjective_entry.get().strip()
    
    # Allow one to three words separated by spaces
    if not re.match(r'^\w+(\s\w+){0,2}$', adjective):
        messagebox.showwarning("Input Error", "Please enter one, two, or three words for the adjective.")
        return

    if not messagebox.askyesno("Confirm Add", f"Are you sure you want to add Rating: {rating}, Adjective: {adjective}?"):
        return
    
    file_exists = os.path.isfile(csv_file_path)
    
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(['Rating', 'Adjective'])
        
        writer.writerow([rating, adjective])
    
    messagebox.showinfo("Success", f"Added Rating: {rating}, Adjective: {adjective}")
    refresh_table()
    clear_form()

def clear_form():
    rating_var.set(rating_options[0])
    adjective_entry.delete(0, tk.END)

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    
    if os.path.isfile(csv_file_path):
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Get the header
            tree["columns"] = header
            tree.heading("#0", text="ID")
            for col in header:
                tree.heading(col, text=col)
                tree.column(col, width=150, anchor=tk.W)
            
            for row in reader:
                tree.insert("", tk.END, values=row)

def remove_selected_record():
    selected_item = tree.selection()
    
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a record to remove.")
        return

    selected_values = tree.item(selected_item[0], 'values')
    rating, adjective = selected_values

    if not messagebox.askyesno("Confirm Remove", f"Are you sure you want to remove Rating: {rating}, Adjective: {adjective}?"):
        return
    
    # Read all records
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
    
    header = lines[0]
    records = lines[1:]
    
    # Find and remove the selected record
    new_records = [line for line in records if not line.strip().endswith(adjective)]
    
    if len(new_records) == len(records):
        messagebox.showwarning("Removal Error", "Selected record not found.")
        return
    
    # Write back to the CSV file without the removed record
    with open(csv_file_path, mode='w', encoding='utf-8') as file:
        file.write(header)
        file.writelines(new_records)
    
    messagebox.showinfo("Success", f"Removed record: Rating: {rating}, Adjective: {adjective}")
    refresh_table()

root = tk.Tk()
root.title("CSV Data Viewer")

root.geometry("600x500")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text="CSV Data Viewer", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

form_frame = tk.Frame(root, bg="#f0f0f0")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Rating:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
rating_options = [1, 2, 3, 4, 5]
rating_var = tk.StringVar(root)
rating_var.set(rating_options[0])
rating_menu = tk.OptionMenu(form_frame, rating_var, *rating_options)
rating_menu.config(width=10)
rating_menu.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Adjective:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5)
adjective_entry = tk.Entry(form_frame, font=("Arial", 12), width=20)
adjective_entry.grid(row=1, column=1, padx=10, pady=5)

add_button = tk.Button(form_frame, text="Add", command=add_record, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

remove_button = tk.Button(form_frame, text="Remove Selected", command=remove_selected_record, font=("Arial", 12), bg="#f44336", fg="white", padx=10, pady=5)
remove_button.grid(row=3, column=0, columnspan=2, pady=10)

table_frame = tk.Frame(root)
table_frame.pack(pady=10)

tree = ttk.Treeview(table_frame, columns=("Rating", "Adjective"), show="headings", height=15)
tree.heading("Rating", text="Rating")
tree.heading("Adjective", text="Adjective")
tree.column("Rating", width=150, anchor=tk.W)
tree.column("Adjective", width=150, anchor=tk.W)

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree.config(yscrollcommand=scrollbar.set)

refresh_table()

root.mainloop()
