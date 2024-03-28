import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

connection = sqlite3.connect("student_details.db")
cursor = connection.cursor()

TABLE_NAME = "students"
STUDENT_NAME = "name"
STUDENT_EDUCATIONALQUALIFICATION = "educationalqualification"
STUDENT_COLLEGE = "college"
STUDENT_GENDER = "gender"
STUDENT_ADDRESS = "address"
STUDENT_PHONE = "phone"  # New field for city

cursor.execute("CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_NAME + " TEXT, " +
                STUDENT_EDUCATIONALQUALIFICATION + " TEXT, " + STUDENT_COLLEGE + " TEXT, " + STUDENT_GENDER + " TEXT, " +
                STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER );")
root = tk.Tk()
root.title("Exam Application")
root.config(bg="#E0BDCF")
titleLabel = tk.Label(root,text="Student Application",bg="#E0BDCF",fg="#7D457A",font=("Times New Roman",30,"bold"))
titleLabel.place(x=510,y=5)

# Labels and Entry widgets for the new city field
nameLabel = tk.Label(root, text="Name:", fg="#7D457A", font=("cambria",20))
nameLabel.place(x=400,y=110)

educationalqualificationLabel = tk.Label(root, text="Educatinalqualification:", fg="#7D457A", font=("cambria",20)) 
educationalqualificationLabel.place(x=400,y=190)

collegeLabel = tk.Label(root, text="College:", fg="#7D457A", font=("cambria",20)) 
collegeLabel.place(x=400,y=260)

genderLabel = tk.Label(root, text="Gender:", fg="#7D457A", font=("cambria",20))  
genderLabel.place(x=400,y=330)

addressLabel = tk.Label(root, text="Address:", fg="#7D457A", font=("cambria",20))  
addressLabel.place(x=400,y=400)

phoneLabel = tk.Label(root, text="Phone:", fg="#7D457A", font=("cambria",20))
phoneLabel.place(x=400,y=480)

nameEntry = tk.Entry(root, font=("cambria",15))
nameEntry.place(x=700,y=115)

educationalqualificationEntry = tk.Entry(root, font=("cambria",15))
educationalqualificationEntry.place(x=700,y=200)

collegeEntry = tk.Entry(root, font=("cambria",15)) 
collegeEntry.place(x=700,y=273)

genderEntry = tk.Entry(root, font=("cambria",15))
genderEntry.place(x=700,y=340)

addressEntry = tk.Entry(root,font=("cambria",15)) 
addressEntry.place(x=700,y=410)

phoneEntry = tk.Entry(root, font=("cambria",15))  
phoneEntry.place(x=700,y=490)

def take_input():
    name = nameEntry.get()
    educationalqualification = educationalqualificationEntry.get()
    college = collegeEntry.get()
    gender = genderEntry.get()
    address = addressEntry.get()
    phone = phoneEntry.get()  # Retrieve city from entry field

    cursor.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_EDUCATIONALQUALIFICATION + ", " +
                    STUDENT_COLLEGE + ", " + STUDENT_GENDER + ", " + STUDENT_ADDRESS + ", " +
                    STUDENT_PHONE + " ) VALUES (?,?,?,?,?,?)",
                    (name, educationalqualification, college, gender, address, phone))

    connection.commit()

    nameEntry.delete(0, 'end')
    educationalqualificationEntry.delete(0, 'end')
    collegeEntry.delete(0, 'end')
    genderEntry.delete(0, 'end')
    addressEntry.delete(0, 'end')
    phoneEntry.delete(0, 'end')  # Clear city entry field

    messagebox.showinfo("Success", "Data Saved Successfully.")

def display_data():
    top = tk.Toplevel(root)
    top.title("Student Details")   

    columns = (STUDENT_NAME, STUDENT_EDUCATIONALQUALIFICATION, STUDENT_COLLEGE, STUDENT_GENDER, STUDENT_ADDRESS, STUDENT_PHONE)
    tree = ttk.Treeview(top, columns=columns, show="headings")
    tree.grid(column=0, row=1)

    tree.heading(STUDENT_NAME, text=STUDENT_NAME)
    tree.heading(STUDENT_EDUCATIONALQUALIFICATION, text=STUDENT_EDUCATIONALQUALIFICATION)
    tree.heading(STUDENT_COLLEGE, text=STUDENT_COLLEGE)
    tree.heading(STUDENT_GENDER, text=STUDENT_GENDER)
    tree.heading(STUDENT_ADDRESS, text=STUDENT_ADDRESS)
    tree.heading(STUDENT_PHONE, text=STUDENT_PHONE)  # Show city in the treeview

    cursor.execute("SELECT * FROM " + TABLE_NAME)
    results = cursor.fetchall()

    for row in results:
        tree.insert('', 'end', values=row)

button = tk.Button(root, text="Add data", command=take_input,font=("cambria",15)) 
button.place(x=500,y=600)

displayButton = tk.Button(root, text="Display Data", command=display_data,font=("cambria",15)) 
displayButton.place(x=700,y=595)

root.mainloop()

