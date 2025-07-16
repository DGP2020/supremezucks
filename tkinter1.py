import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
root=tk.Tk()
root.title("Tkinter GUI program")
#Task1

welcome_label=tk.Label(root,text="Welcome to tkinter")
welcome_label.pack(pady=10)
def welcome_message():
    messagebox.showinfo("Welcome","Welcome Button Clicked!")

welcome_button=tk.Button(root,text="Welcome",command=welcome_message)
welcome_button.pack(pady=5)
exit_button=tk.Button(root,text="Exit",command=root.quit)
exit_button.pack(pady=5)
#Task2
combo_label=tk.Label(root,text="Choose an option:")
combo_label.pack(pady=10)
options =["Option1","Option2","Option3"]
combo=ttk.Combobox(root,values=options)
combo.pack()

check_button_var=tk.BooleanVar()
check_button=tk.Checkbutton(root,text="Check me",variable=check_button_var)
check_button.pack()
#Task3
def display_info():
    name=name_entry.get()
    branch=branch_entry.get()
    year=year_entry.get()
    messagebox.showinfo("Info",f"Name:{name},Branch:{branch},Year:{year}")

name_label=tk.Label(root,text="Enter name")
name_label.pack(pady=5)
name_entry=tk.Entry(root)
name_entry.pack()

branch_label=tk.Label(root,text="Enter Branch")
branch_label.pack(pady=5)
branch_entry=tk.Entry(root)
branch_entry.pack()

year_label=tk.Label(root,text="Enter year")
year_label.pack(pady=5)
year_entry=tk.Entry(root)
year_entry.pack()

submit_button=tk.Button(root,text="Submit",command=display_info)
submit_button.pack(pady=10)

#Task 4a
scrolled_text_label=tk.Label(root,text="Scrolled text widget")
scrolled_text_label.pack(pady=5)
scrolled_text=ScrolledText(root,width=40,height=5)
scrolled_text.pack()

#Task 4b
progress_label=tk.Label(root,text="Progress Bar")
progress_label.pack(pady=5)
progress=ttk.Progressbar(root,length=200)
progress.pack(pady=5) 
progress['value']=50

#Task4c
listbox_label = tk.Label(root, text="List Box")
listbox_label.pack(pady=5)
listbox = tk.Listbox(root)
listbox.pack(pady=5)
listbox.insert(1, "IPF")
listbox.insert(2, "IDEA LAB")
listbox.insert(3, "AD LAB")
root.mainloop()
"""
# Task 5: Text widget with string insertion and deletion
text_label = tk.Label(root, text="Text Widget")
text_label.pack(pady=5)
text_widget = tk.Text(root, height=2, width=30)
text_widget.pack(pady=5)

# Insert a string at the beginning and end, then delete first and last characters
initial_string = "Tkinter GUI Program"
text_widget.insert('1.0', initial_string)

def modify_text():
    text_content = text_widget.get('1.0', 'end-1c')
    modified_text = text_content[1:-1]  # Remove first and last characters
    text_widget.delete('1.0', 'end')
    text_widget.insert('1.0', modified_text)

modify_button = tk.Button(root, text="Modify Text", command=modify_text)
modify_button.pack(pady=5)
"""


