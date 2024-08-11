import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
import re

csv_file_path = 'rating_comments.csv'

placeholder_added = False

def add_record(rating, comment):
    # Check if the file exists
    file_exists = os.path.isfile(csv_file_path)

    # Open the file to check for duplicate entry
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        if file_exists:
            next(reader)  # Skip the header
            for row in reader:
                if row == [rating, comment]:
                    messagebox.showwarning("Duplicate Record", "This record already exists.")
                    return

    # Add record if no duplicate found
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Rating', 'Comment Template'])
        writer.writerow([rating, comment])
    
    messagebox.showinfo("Success", f"Added Rating: {rating}, Comment: {comment}")
    refresh_table()

def remove_selected_record():
    selected_item = tree.selection()
    
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a record to remove.")
        return
    
    selected_record = tree.item(selected_item)['values']
    rating, comment = selected_record
    
    if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to remove the record: Rating: {rating}, Comment: {comment}?"):
        # Read all lines from the file
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Separate the header and records
        header = lines[0]
        records = lines[1:]
        
        # Remove the selected record
        updated_records = [line for line in records if not (line.strip().startswith(rating) and line.strip().endswith(comment))]
        
        # Check if record was found
        if len(updated_records) == len(records):
            messagebox.showwarning("Removal Error", "Selected record not found.")
            return
        
        # Write the updated records back to the file
        with open(csv_file_path, mode='w', encoding='utf-8') as file:
            file.write(header)
            file.writelines(updated_records)
        
        messagebox.showinfo("Success", f"Removed record: Rating: {rating}, Comment: {comment}")
        refresh_table()

def submit_record():
    rating = rating_var.get()
    comment = comment_text.get("1.0", tk.END).strip()
    
    if rating and comment:
        if validate_comment(comment):
            if messagebox.askyesno("Confirm Addition", f"Are you sure you want to add the record: Rating: {rating}, Comment: {comment}?"):
                add_record(rating, comment)
                clear_form()
        else:
            messagebox.showwarning("Input Error", "The comment must contain exactly one valid '{adjective}' placeholder.")
    else:
        messagebox.showwarning("Input Error", "Please select a rating and enter a comment.")

def insert_placeholder():
    global placeholder_added
    current_text = comment_text.get("1.0", tk.END).strip()
    
    if re.search(r'\{adjective\}', current_text):
        messagebox.showinfo("Placeholder Exists", "Placeholder '{adjective}' already exists in the comment.")
        return
    
    if not placeholder_added:
        new_text = f"{current_text} {{adjective}}"
        comment_text.delete("1.0", tk.END)
        comment_text.insert("1.0", new_text)
        placeholder_added = True
    else:
        messagebox.showinfo("Placeholder Added", "Placeholder '{adjective}' can only be added once.")

def validate_comment(comment):
    return re.fullmatch(r'[^{}]*\{adjective\}[^{}]*', comment) and comment.count('{adjective}') == 1

def clear_form():
    global placeholder_added
    rating_var.set(rating_options[0])
    comment_text.delete("1.0", tk.END)
    placeholder_added = False

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    
    if os.path.isfile(csv_file_path):
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header
            
            for row in reader:
                tree.insert("", tk.END, values=row)

# Create the main window
root = tk.Tk()
root.title("Comment Template Modifier")

root.geometry("600x700")
root.config(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Input Form", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky='w')

# Instructions label
instructions_label = tk.Label(root, text="Fill out the form below and click Submit to add a record to the CSV file.", bg="#f0f0f0")
instructions_label.grid(row=1, column=0, columnspan=2, padx=20, pady=5, sticky='w')

# Rating label and menu
tk.Label(root, text="Rating:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=20, pady=5, sticky='w')
rating_options = [1, 2, 3, 4, 5]
rating_var = tk.StringVar(root)
rating_var.set(rating_options[0])
rating_menu = tk.OptionMenu(root, rating_var, *rating_options)
rating_menu.config(width=10)
rating_menu.grid(row=3, column=0, padx=20, pady=5, sticky='w')

# Comment label and text area
tk.Label(root, text="Comment Template:", font=("Arial", 12), bg="#f0f0f0").grid(row=4, column=0, padx=20, pady=5, sticky='w')
comment_text = tk.Text(root, width=90, height=8, font=("Arial", 12))
comment_text.grid(row=5, column=0, padx=20, pady=10, sticky='w')

# Button frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.grid(row=6, column=0, padx=20, pady=10, sticky='w')

# Add placeholder button
add_placeholder_button = tk.Button(button_frame, text="Add Placeholder", command=insert_placeholder, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
add_placeholder_button.pack(side=tk.LEFT, padx=5)

# Submit button
submit_button = tk.Button(button_frame, text="Submit", command=submit_record, font=("Arial", 12), bg="#2196F3", fg="white", padx=10, pady=5)
submit_button.pack(side=tk.LEFT, padx=5)

# Clear button
clear_button = tk.Button(button_frame, text="Clear", command=clear_form, font=("Arial", 12), bg="#f44336", fg="white", padx=10, pady=5)
clear_button.pack(side=tk.LEFT, padx=5)

# Remove selected button
remove_button = tk.Button(button_frame, text="Remove Selected", command=remove_selected_record, font=("Arial", 12), bg="#FFC107", fg="black", padx=10, pady=5)
remove_button.pack(side=tk.LEFT, padx=5)

# Table label
tk.Label(root, text="Templates:", font=("Arial", 12), bg="#f0f0f0").grid(row=7, column=0, padx=20, pady=10, sticky='w')

# Table for displaying records
table_frame = tk.Frame(root)
table_frame.grid(row=8, column=0, padx=20, pady=10, sticky='nsew')

tree = ttk.Treeview(table_frame, columns=("Rating", "Comment Template"), show="headings", height=15)
tree.heading("Rating", text="Rating")
tree.heading("Comment Template", text="Comment Template")
tree.column("Rating", width=100, anchor=tk.CENTER)
tree.column("Comment Template", width=450, anchor=tk.W)

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree.config(yscrollcommand=scrollbar.set)

# Initial table refresh
refresh_table()

# Configure window resizing
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(8, weight=1)

# Start the Tkinter event loop
root.mainloop()
