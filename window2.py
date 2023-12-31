import tkinter as tk
import tkinter.font as tkFont
from tkinter import StringVar
import tkinter.messagebox
import databases
from tkinter import *
from datetime import datetime
from datastorage import DataStorage

# Input the generated front from the design application you created thru paper

class App:
    def __init__(self, root):
        # setting title
        root.title("Contact Tracing App")
        width = 842
        height = 650
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        # Title Block
        TitleBlock = tk.Label(root)
        ft = tkFont.Font(family='Times', size=22)
        TitleBlock["font"] = ft
        TitleBlock["fg"] = "#333333"
        TitleBlock["justify"] = "center"
        TitleBlock["text"] = "Contact Tracing Form"
        TitleBlock.place(x=280, y=10)

        # NAME TEXT FIELD
        def on_entry_focus_in1(event):
            if user_name.get() == placeholder_text1:
                user_name.delete(0, tk.END)
                user_name.configure(show="")
                user_name.configure(fg="#333333")

        def on_entry_focus_out1(event):
            if user_name.get() == "":
                user_name.insert(0, placeholder_text1)
                user_name.configure(fg="gray")
        
        self.name = StringVar(value="")

        user_name = tk.Entry(root)
        user_name["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        user_name["font"] = ft
        user_name["fg"] = "gray"
        user_name["justify"] = "left"
        user_name["text"] = "Name"
        user_name["textvariable"] = self.name
        user_name.place(x=30, y=60, width=279, height=30)

        placeholder_text1 = "Full Name"
        user_name.insert(0, placeholder_text1)
        user_name.bind("<FocusIn>", on_entry_focus_in1)
        user_name.bind("<FocusOut>", on_entry_focus_out1)

        # STUDENT NUMBER TEXT FIELD

        def on_entry_focus_in2(event):
            if stdnum.get() == placeholder_text2:
                stdnum.delete(0, tk.END)
                stdnum.configure(show="")
                stdnum.configure(fg="#333333")

        def on_entry_focus_out2(event):
            if stdnum.get() == "":
                stdnum.insert(0, placeholder_text2)
                stdnum.configure(fg="gray")
        
        self.studentnum = StringVar(value="")


        stdnum = tk.Entry(root)
        stdnum["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        stdnum["font"] = ft
        stdnum["fg"] = "gray"
        stdnum["justify"] = "left"
        stdnum["text"] = "Student Number"
        stdnum["textvariable"] = self.studentnum
        stdnum.place(x=30, y=100, width=279, height=30)

        placeholder_text2 = "Student Number"
        stdnum.insert(0, placeholder_text2)
        stdnum.bind("<FocusIn>", on_entry_focus_in2)
        stdnum.bind("<FocusOut>", on_entry_focus_out2)

        # QUESTION 1
        quest1 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        quest1["font"] = ft
        quest1["fg"] = "#333333"
        quest1["justify"] = "left"
        quest1["text"] = "1. Have you been vaccinated for COVID-19? *"
        quest1["wraplength"]= 350
        quest1.place(x=30, y=140)
        quest1["justify"] = "left"

        self.question1 = StringVar(value="0")

        op1q1 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op1q1["font"] = ft
        op1q1["fg"] = "#333333"
        op1q1["justify"] = "left"
        op1q1["text"] = "Not Yet"
        op1q1["variable"] = self.question1
        op1q1["value"] = "Not Yet"
        op1q1.place(x=60, y=180, height=25)

        op2q1 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op2q1["font"] = ft
        op2q1["fg"] = "#333333"
        op2q1["justify"] = "left"
        op2q1["text"] = "1st Dose"
        op2q1["variable"] = self.question1
        op2q1["value"] = "1st Dose"
        op2q1.place(x=60, y=200, height=25)

        op3q1 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op3q1["font"] = ft
        op3q1["fg"] = "#333333"
        op3q1["justify"] = "left"
        op3q1["text"] = "2nd Dose (Fully Vaccinated)"
        op3q1["variable"] = self.question1
        op3q1["value"] = "2nd Dose (Fully Vaccinated)"
        op3q1.place(x=60, y=220, height=25)

        op4q1 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op4q1["font"] = ft
        op4q1["fg"] = "#333333"
        op4q1["justify"] = "left"
        op4q1["text"] = "1st Booster Shot"
        op4q1["variable"] = self.question1
        op4q1["value"] = "1st Booster Shot"
        op4q1.place(x=60, y=240, height=25)

        op5q1 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op5q1["font"] = ft
        op5q1["fg"] = "#333333"
        op5q1["justify"] = "left"
        op5q1["text"] = "2nd Booster Shot"
        op5q1["variable"] = self.question1
        op5q1["value"] = "2nd Booster Shot"
        op5q1.place(x=60, y=260, height=25)

        # QUESTION 2
        quest2 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        quest2["font"] = ft
        quest2["fg"] = "#333333"
        quest2["justify"] = "left"
        quest2["text"] = "2. Are you experiencing any symptoms in the past 7 days such as:*"
        quest2["wraplength"]= 350
        quest2.place(x=30, y=290)

        self.question2 = StringVar(value="0")

        op1q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op1q2["font"] = ft
        op1q2["fg"] = "#333333"
        op1q2["justify"] = "left"
        op1q2["text"] = "Fever"
        op1q2.place(x=60, y=340)
        op1q2["variable"] = self.question2
        op1q2["value"] = "Fever"

        op2q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op2q2["font"] = ft
        op2q2["fg"] = "#333333"
        op2q2["justify"] = "left"
        op2q2["text"] = "Cough"
        op2q2.place(x=60, y=360)
        op2q2["variable"] = self.question2
        op2q2["value"] = "Cough"

        op3q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op3q2["font"] = ft
        op3q2["fg"] = "#333333"
        op3q2["justify"] = "left"
        op3q2["text"] = "Colds"
        op3q2.place(x=60, y=380)
        op3q2["variable"] = self.question2
        op3q2["value"] = "Colds"

        op4q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op4q2["font"] = ft
        op4q2["fg"] = "#333333"
        op4q2["justify"] = "left"
        op4q2["text"] = "Muscle/body pains"
        op4q2.place(x=60, y=400)
        op4q2["variable"] = self.question2
        op4q2["value"] = "Muscle/body pains"

        op5q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op5q2["font"] = ft
        op5q2["fg"] = "#333333"
        op5q2["justify"] = "left"
        op5q2["text"] = "Sore throat"
        op5q2.place(x=60, y=420)
        op5q2["variable"] = self.question2
        op5q2["value"] = "Sore throat"

        op6q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op6q2["font"] = ft
        op6q2["fg"] = "#333333"
        op6q2["justify"] = "left"
        op6q2["text"] = "Diarrhea"
        op6q2.place(x=60, y=440)
        op6q2["variable"] = self.question2
        op6q2["value"] = "Diarrhea"

        op7q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op7q2["font"] = ft
        op7q2["fg"] = "#333333"
        op7q2["justify"] = "left"
        op7q2["text"] = "Headache"
        op7q2.place(x=200, y=340)
        op7q2["variable"] = self.question2
        op7q2["value"] = "Headache"

        op8q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op8q2["font"] = ft
        op8q2["fg"] = "#333333"
        op8q2["justify"] = "left"
        op8q2["text"] = "Shortness of breath"
        op8q2.place(x=200, y=360)
        op8q2["variable"] = self.question2
        op8q2["value"] = "Shortness of breath"

        op9q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op9q2["font"] = ft
        op9q2["fg"] = "#333333"
        op9q2["justify"] = "left"
        op9q2["text"] = "Difficulty of breathing"
        op9q2.place(x=200, y=380)
        op9q2["variable"] = self.question2
        op9q2["value"] = "Difficulty of breathing"

        op10q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op10q2["font"] = ft
        op10q2["fg"] = "#333333"
        op10q2["justify"] = "left"
        op10q2["text"] = "Loss of taste"
        op10q2.place(x=200, y=400)
        op10q2["variable"] = self.question2
        op10q2["value"] = "Loss of taste"

        op11q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op11q2["font"] = ft
        op11q2["fg"] = "#333333"
        op11q2["justify"] = "left"
        op11q2["text"] = "Loss of smell"
        op11q2.place(x=200, y=420)
        op11q2["variable"] = self.question2
        op11q2["value"] = "Loss of smell"

        op12q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op12q2["font"] = ft
        op12q2["fg"] = "#333333"
        op12q2["justify"] = "left"
        op12q2["text"] = "None of the above"
        op12q2.place(x=200, y=440)
        op12q2["variable"] = self.question2
        op12q2["value"] = "None of the above"
        
        # QUESTION 3
        quest3 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        quest3["font"] = ft
        quest3["fg"] = "#333333"
        quest3["justify"] = "left"
        quest3["text"] = "3. Have you had exposure to a probable or confirmed case in the last 14 days?*"
        quest3["wraplength"] = 350
        quest3.place(x=30, y=490)

        self.question3 = StringVar(value="0")

        op1q3 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op1q3["font"] = ft
        op1q3["fg"] = "#333333"
        op1q3["justify"] = "left"
        op1q3["text"] = "Yes"
        op1q3["value"] = "Yes"
        op1q3["variable"] = self.question3
        op1q3.place(x=60, y=530)

        op2q3 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op2q3["font"] = ft
        op2q3["fg"] = "#333333"
        op2q3["justify"] = "left"
        op2q3["text"] = "No"
        op2q3["value"] = "No"
        op2q3["variable"] = self.question3
        op2q3.place(x=60, y=550)

        op3q3 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op3q3["font"] = ft
        op3q3["fg"] = "#333333"
        op3q3["justify"] = "left"
        op3q3["text"] = "Uncertain"
        op3q3["value"] = "Uncertain"
        op3q3["variable"] = self.question3
        op3q3.place(x=60, y=570)
       
       # QUESTION 4
        quest4 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        quest4["font"] = ft
        quest4["fg"] = "#333333"
        quest4["justify"] = "left"
        quest4["text"] = "4. Have you had in contact with somebody with body pains, headache, sore throat, fever, diarrhea, cough, colds, shortness of breath, loss of taste, or loss of smell in the past 7 days? *"
        quest4["wraplength"] = 350
        quest4.place(x=430, y=55)

        self.question4 = StringVar(value="0")

        op1q4 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op1q4["font"] = ft
        op1q4["fg"] = "#333333"
        op1q4["justify"] = "center"
        op1q4["text"] = "Yes"
        op1q4["value"] = "Yes"
        op1q4["variable"] = self.question4
        op1q4.place(x=490, y=130)

        op2q4 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op2q4["font"] = ft
        op2q4["fg"] = "#333333"
        op2q4["justify"] = "center"
        op2q4["text"] = "No"
        op2q4["value"] = "No"
        op2q4["variable"] = self.question4
        op2q4.place(x=490, y=150)

       # QUESTION 5
        quest5 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        quest5["font"] = ft
        quest5["fg"] = "#333333"
        quest5["justify"] = "left"
        quest5["text"] = "5. Have you been tested for Covid-19 in the last 14 days?*"
        quest5.place(x=430, y=175, width=332, height=30)

        self.question5 = StringVar(value="0")

        op1q5 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op1q5["font"] = ft
        op1q5["fg"] = "#333333"
        op1q5["justify"] = "center"
        op1q5["text"] = "Yes, Possitive"
        op1q5["value"] = "Yes, Possitive"
        op1q5["variable"] = self.question5
        op1q5.place(x=490, y=210)

        op2q5 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op2q5["font"] = ft
        op2q5["fg"] = "#333333"
        op2q5["justify"] = "center"
        op2q5["text"] = "Yes, Negative"
        op2q5["value"] = "Yes, Negative"
        op2q5["variable"] = self.question5
        op2q5.place(x=490, y=230)

        op3q5 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op3q5["font"] = ft
        op3q5["fg"] = "#333333"
        op3q5["justify"] = "center"
        op3q5["text"] = "Yes, Pending"
        op3q5["value"] = "Yes, Pending"
        op3q5["variable"] = self.question5
        op3q5.place(x=620, y=210)

        op4q5 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op4q5["font"] = ft
        op4q5["fg"] = "#333333"
        op4q5["justify"] = "center"
        op4q5["text"] = "No"
        op4q5["value"] = "No"
        op4q5["variable"] = self.question5
        op4q5.place(x=620, y=230)

        # Respondent Details
        respo_det = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        respo_det["font"] = ft
        respo_det["fg"] = "#333333"
        respo_det["justify"] = "center"
        respo_det["text"] = "Respondent Details:"
        respo_det.place(x=530, y=270, width=135, height=30)

        # Email Address

        def on_entry_focus_in3(event):
            if email_add.get() == placeholder_text3:
                email_add.delete(0, tk.END)
                email_add.configure(show="")
                email_add.configure(fg="#333333")

        def on_entry_focus_out3(event):
            if email_add.get() == "":
                email_add.insert(0, placeholder_text3)
                email_add.configure(fg="gray")

        self.emailadd = StringVar(value="")


        email_add = tk.Entry(root)
        email_add["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        email_add["font"] = ft
        email_add["fg"] = "gray"
        email_add["justify"] = "left"
        email_add["text"] = "Email Address"
        email_add["textvariable"] = self.emailadd
        email_add.place(x=460, y=310, width=281, height=30)

        placeholder_text3 = "Email Address"
        email_add.insert(0, placeholder_text3)
        email_add.bind("<FocusIn>", on_entry_focus_in3)
        email_add.bind("<FocusOut>", on_entry_focus_out3)

        # Contact Number

        def on_entry_focus_in4(event):
            if cont_num.get() == placeholder_text4:
                cont_num.delete(0, tk.END)
                cont_num.configure(show="")
                cont_num.configure(fg="#333333")

        def on_entry_focus_out4(event):
            if cont_num.get() == "":
                cont_num.insert(0, placeholder_text4)
                cont_num.configure(fg="gray")

        self.contactnumb = StringVar(value="")


        cont_num = tk.Entry(root)
        cont_num["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        cont_num["font"] = ft
        cont_num["fg"] = "gray"
        cont_num["justify"] = "left"
        cont_num["text"] = "Contact Number"
        cont_num["textvariable"] = self.contactnumb
        cont_num.place(x=460, y=350, width=281, height=30)

        placeholder_text4 = "Contact Number"
        cont_num.insert(0, placeholder_text4)
        cont_num.bind("<FocusIn>", on_entry_focus_in4)
        cont_num.bind("<FocusOut>", on_entry_focus_out4)

        # Contact Person Details

        conper_det = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        conper_det["font"] = ft
        conper_det["fg"] = "#333333"
        conper_det["justify"] = "center"
        conper_det["text"] = "Contact Person Details:"
        conper_det.place(x=500, y=390, width=185, height=30)

        # Contact Person Name 
        def on_entry_focus_in5(event):
            if conper_name.get() == placeholder_text5:
                conper_name.delete(0, tk.END)
                conper_name.configure(show="")
                conper_name.configure(fg="#333333")

        def on_entry_focus_out5(event):
            if conper_name.get() == "":
                conper_name.insert(0, placeholder_text5)
                conper_name.configure(fg="gray")

        self.contactpersonname = StringVar(value="")

        conper_name = tk.Entry(root)
        conper_name["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        conper_name["font"] = ft
        conper_name["fg"] = "gray"
        conper_name["justify"] = "left"
        conper_name["text"] = "Contact Person Name"
        conper_name["textvariable"] = self.contactpersonname
        conper_name.place(x=460, y=430, width=280, height=30)

        placeholder_text5 = "Contact Person's Full Name"
        conper_name.insert(0, placeholder_text5)
        conper_name.bind("<FocusIn>", on_entry_focus_in5)
        conper_name.bind("<FocusOut>", on_entry_focus_out5)

        # Contact Person Number
        def on_entry_focus_in6(event):
            if conper_num.get() == placeholder_text6:
                conper_num.delete(0, tk.END)
                conper_num.configure(show="")
                conper_num.configure(fg="#333333")

        def on_entry_focus_out6(event):
            if conper_num.get() == "":
                conper_num.insert(0, placeholder_text6)
                conper_num.configure(fg="gray")

        self.contactpersonnumber = StringVar(value="")

        conper_num = tk.Entry(root)
        conper_num["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        conper_num["font"] = ft
        conper_num["fg"] = "gray"
        conper_num["justify"] = "left"
        conper_num["text"] = "Contact Person Number"
        conper_num["textvariable"] = self.contactpersonnumber
        conper_num.place(x=460, y=470, width=280, height=30)

        placeholder_text6 = "Contact Person's Phone Number"
        conper_num.insert(0, placeholder_text6)
        conper_num.bind("<FocusIn>", on_entry_focus_in6)
        conper_num.bind("<FocusOut>", on_entry_focus_out6) 

        # Contact Person Email Address
        
        def on_entry_focus_in7(event):
            if conper_email.get() == placeholder_text7:
                conper_email.delete(0, tk.END)
                conper_email.configure(show="")
                conper_email.configure(fg="#333333")

        def on_entry_focus_out7(event):
            if conper_email.get() == "":
                conper_email.insert(0, placeholder_text7)
                conper_email.configure(fg="gray")

        self.contactpersonemail = StringVar(value="")

        conper_email = tk.Entry(root)
        conper_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        conper_email["font"] = ft
        conper_email["fg"] = "gray"
        conper_email["justify"] = "left"
        conper_email["text"] = "Contact Person Email"
        conper_email["textvariable"] = self.contactpersonemail
        conper_email.place(x=460, y=510, width=280, height=30)

        placeholder_text7 = "Contact Person's Email Address"
        conper_email.insert(0, placeholder_text7)
        conper_email.bind("<FocusIn>", on_entry_focus_in7)
        conper_email.bind("<FocusOut>", on_entry_focus_out7)

        # Relationship to the Contact Person

        def on_entry_focus_in8(event):
            if rs_to_conper.get() == placeholder_text8:
                rs_to_conper.delete(0, tk.END)
                rs_to_conper.configure(show="")
                rs_to_conper.configure(fg="#333333")

        def on_entry_focus_out8(event):
            if rs_to_conper.get() == "":
                rs_to_conper.insert(0, placeholder_text8)
                rs_to_conper.configure(fg="gray")

        self.rstoconper = StringVar(value="")

        rs_to_conper = tk.Entry(root)
        rs_to_conper["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        rs_to_conper["font"] = ft
        rs_to_conper["fg"] = "gray"
        rs_to_conper["justify"] = "left"
        rs_to_conper["text"] = "Relationship to the Contact Person"
        rs_to_conper["textvariable"] = self.rstoconper
        rs_to_conper.place(x=460, y=550, width=279, height=30)

        placeholder_text8 = "Relationship to the Contact Person"
        rs_to_conper.insert(0, placeholder_text8)
        rs_to_conper.bind("<FocusIn>", on_entry_focus_in8)
        rs_to_conper.bind("<FocusOut>", on_entry_focus_out8)

        # Buttons

        def records():
            answer = tkinter .messagebox.askyesno(
                title="Confirmation", message="Checking Records?")
            if answer:
                root.destroy()
                root2 = Tk()
                app = databases.datas(root2)
                root2.focus_force()
                root2.mainloop()
        recordmanager_button = tk.Button(root , command=lambda: records())
        recordmanager_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        recordmanager_button["font"] = ft
        recordmanager_button["fg"] = "#000000"
        recordmanager_button["justify"] = "center"
        recordmanager_button["text"] = "File Records"
        recordmanager_button.place(x=460, y=600, width=70, height=25)

        def iExit():
            answer = tkinter.messagebox.askyesno(
                title="Confirmation", message="Are you sure you want to quit?")
            if answer:
                root.destroy()

        exit_button = tk.Button(root , command=lambda: iExit())
        exit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        exit_button["font"] = ft
        exit_button["fg"] = "#000000"
        exit_button["justify"] = "center"
        exit_button["text"] = "Exit"
        exit_button.place(x=560, y=600, width=70, height=25)

        def clearForm():

            self.name.set("")
            user_name.insert(0, placeholder_text1)
            user_name.configure(fg="gray")

            self.studentnum.set("")
            stdnum.configure(fg="gray")
            stdnum.insert(0, placeholder_text2)

            self.question1.set(0)
            self.question2.set(0)
            self.question3.set(0)
            self.question4.set(0)
            self.question5.set(0)

            self.emailadd.set("")
            email_add.insert(0, placeholder_text3)
            email_add.configure(fg="gray")

            self.contactnumb.set("")
            cont_num.insert(0, placeholder_text4)
            cont_num.configure(fg="gray")

            self.contactpersonname.set("")
            conper_name.insert(0, placeholder_text5)
            conper_name.configure(fg="gray")

            self.contactpersonnumber.set("")
            conper_num.insert(0, placeholder_text6)
            conper_num.configure(fg="gray")

            self.contactpersonemail.set("")
            conper_email.insert(0, placeholder_text7)
            conper_email.configure(fg="gray")

            self.rstoconper.set("")
            rs_to_conper.insert(0, placeholder_text8)
            rs_to_conper.configure(fg="gray")

        # Manipulating how submit button collect infos
        def submitForm(user_name, stdnum, question1, question2, question3, question4, question5, email_add, cont_num, conper_name, conper_num, conper_email, rs_to_conper):
            question1Answer = question1.get()
            question2Answer = question2.get()
            question3Answer = question3.get()
            question4Answer = question4.get()
            question5Answer = question5.get()

            nameAnswer = user_name.get()
            studentNumberAnswer = stdnum.get()
            emailAddAnswer = email_add.get()
            contactNumberAnswer = cont_num.get()
            contactPersonNameAnswer = conper_name.get()
            contactPersonNumberAnswer = conper_num.get()
            contactPersonaEmailAddressAnswer = conper_email.get()
            rstoconperAnswer = rs_to_conper.get()

            if (not user_name.get() or nameAnswer == "Full Name" or not stdnum.get() or studentNumberAnswer == "Student Number" or question1Answer == "0"
                    or question2Answer == "0" or question3Answer == "0" or question4Answer == "0" or question5Answer == "0"
                    or not email_add.get() or emailAddAnswer == "Email Address" or not cont_num.get() or contactNumberAnswer == "Contact Number"
                    or not conper_name.get() or contactPersonNameAnswer == "Contact Person's Full Name" or not conper_num.get() or contactPersonNumberAnswer == "Contact Person's Phone Number"
                    or not conper_email.get() or contactPersonaEmailAddressAnswer == "Contact Person's Email Address" or not rs_to_conper.get() or rstoconperAnswer == "Relationship to the Contact Person"):
                tk.messagebox.showerror(
                    title="WARNING", message="Please fill in all fields")
            else:
                answer = tkinter.messagebox.askyesno(
                    title="Confirmation", message="Do you wish to proceed?")
                if answer:
                    data = [nameAnswer,
                            studentNumberAnswer,
                            question1Answer,
                            question2Answer,
                            question3Answer,
                            question4Answer,
                            question5Answer,
                            emailAddAnswer,
                            contactNumberAnswer,
                            contactPersonNameAnswer,
                            contactPersonNumberAnswer,
                            contactPersonaEmailAddressAnswer,
                            rstoconperAnswer
                            ]

                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    data.append(current_time)

                    questions = [
                        "Full Name",
                        "Stud Num",
                        "Q1",
                        "Q2",
                        "Q3",
                        "Q4",
                        "Q5",
                        "Email add",
                        "Contact num",
                        "Contact Person Full Name",
                        "Contact Person Number",
                        "Contact Person's Email Address",
                        "Relationship",
                        "Submit Time"
                    ]

                    DataStorage.save_data('database.csv', questions, data)

                    tkinter.messagebox.showinfo(
                        title="Contact Tracing App", message="Form successfully saved.")
                    clearForm()
                    root.focus()
                       
        sub_button = tk.Button(root)
        sub_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        sub_button["font"] = ft
        sub_button["fg"] = "#000000"
        sub_button["justify"] = "center"
        sub_button["text"] = "Submit"
        sub_button.place(x=660, y=600, width=70, height=25)
        sub_button["command"] = lambda: submitForm(
            self.name, self.studentnum, self.question1, self.question2, self.question3, self.question4, self.question5, self.emailadd, self. contactnumb, self.contactpersonname, self.contactpersonnumber, self.contactpersonemail, self.rstoconper)

        # Program Runner           
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.focus()
    root.mainloop()