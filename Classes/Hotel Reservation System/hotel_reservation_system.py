from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox
from datetime import datetime
import winsound


class Hotel:

    def __init__(self, master):
        self.master = master
        self.master.title("Hotel Management System")
        self.master.geometry('1360x768+0+0')
        self.master.config(background='powder blue')

        mainframe = Frame(self.master)
        mainframe.grid()

        titleframe = Frame(mainframe, width=1360, height=70, bg='powder blue', padx=10)
        titleframe.pack(side=TOP, fill=X)

        topframe = Frame(mainframe, width=1350, height=540, bd=8, relief=RIDGE, bg='cadet blue', padx=10)
        topframe.pack(side=TOP)

        leftframe = Frame(topframe, width=450, height=540, bd=5, relief=RIDGE, bg='powder blue', padx=2)
        leftframe.pack(side=LEFT)

        rightframe = Frame(topframe, width=950, height=540, bd=5, relief=RIDGE, bg='cadet blue', padx=2)
        rightframe.pack(side=RIGHT)

        bottomframe = Frame(mainframe, width=1340, height=150, bd=5, relief=RIDGE, bg='powder blue', padx=10)
        bottomframe.pack(side=BOTTOM)

        # Functions for Buttons
        def i_exit():
            winsound.PlaySound('tick.wav', winsound.SND_ASYNC)
            answer = tkinter.messagebox.askquestion(title='Exit', message='Do you want to exit the application?')
            if answer == 'yes':
                root.destroy()
                return

        def save_receipt():
            f = filedialog.asksaveasfile(mode='w', defaultextension='.doc')
            f.write(self.txt_receipt.get(1.0, END))
            f.close()

        def receipt():
            winsound.PlaySound('tick.wav', winsound.SND_ASYNC)
            self.txt_receipt.insert(END, '\t\t\t  Customer Ref. No - ' + customer_ref.get() + '\n\n' + 'Name - ' +
                                    first_name.get() + ' ' + last_name.get() + '.\t\t\t\t' + 'Identity Proof - '
                                    + identity.get() + '\n' + 'Mobile No. - ' + mobile.get() + '\n' + 'Email id - ' +
                                    email.get() + '\n' + '\n\n' + 'Check In Date - ' + check_in_date.get() + '\t\t\t' +
                                    'Check out Date - ' + check_out_date.get() + '\n' + 'Room No. - ' +
                                    room_no.get() + '\t\t\t\t\t' + 'Room type - ' + room_type.get() + '\n' +
                                    'Sub Total(Rs.) - ' + sub_total.get()
                                    + '\n' + 'Tax Paid(Rs.) - ' + tax_paid.get() + '\n\n' + 'Total(Rs.) - ' +
                                    total_cost.get() + '\n\n' + 'Cash Paid by - ' + money_paid_by.get())

        def reset():
            winsound.PlaySound('tick.wav', winsound.SND_ASYNC)
            customer_ref.set('')
            first_name.set('')
            last_name.set('')
            address.set('')
            pin_code.set('')
            mobile.set('')
            email.set('')
            nationality.set('')
            date_of_birth.set('')
            identity.set('')
            gender.set('')
            check_in_date.set('')
            check_out_date.set('')
            meal.set('')
            room_type.set('')
            room_no.set('')
            room_ext_no.set('')
            no_of_days.set('')
            tax_paid.set('')
            sub_total.set('')
            total_cost.set('')
            money_paid_by.set('')
            self.txt_receipt.delete('1.0', END)

        def total_cost_and_days():
            winsound.PlaySound('tick.wav', winsound.SND_ASYNC)
            in_date = check_in_date.get()
            out_date = check_out_date.get()
            in_date = datetime.strptime(in_date, '%d/%m/%Y')
            out_date = datetime.strptime(out_date, '%d/%m/%Y')
            no_of_days.set(abs(out_date-in_date).days)

            r_type = {'Single': 1200, 'Double': 1500, 'Family': 2000}
            f_type = {'Single': {'Breakfast': 15, 'Lunch': 50, 'Dinner': 50},
                      'Double': {'Breakfast': 25, 'Lunch': 80, 'Dinner': 80},
                      'Family': {'Breakfast': 40, 'Lunch': 100, 'Dinner': 100}}

            q1 = float(r_type[room_type.get()])
            q2 = float(f_type[room_type.get()][meal.get()])
            q3 = float(q1+q2)
            q4 = float(q3*float(no_of_days.get()))
            q5 = float(q4*0.2)
            q6 = q4+q5
            tax = str(q5)
            sub_t = str(q4)
            total_c = str(q6)
            tax_paid.set(tax)
            sub_total.set(sub_t)
            total_cost.set(total_c)

        customer_ref = StringVar()
        first_name = StringVar()
        last_name = StringVar()
        address = StringVar()
        pin_code = StringVar()
        mobile = StringVar()
        email = StringVar()
        nationality = StringVar()
        date_of_birth = StringVar()
        identity = StringVar()
        gender = StringVar()
        check_in_date = StringVar()
        check_out_date = StringVar()
        meal = StringVar()
        room_type = StringVar()
        room_no = StringVar()
        room_ext_no = StringVar()
        no_of_days = StringVar()
        tax_paid = StringVar()
        sub_total = StringVar()
        total_cost = StringVar()
        money_paid_by = StringVar()

        # Title
        self.lbl_title = Label(titleframe, font=('calibry', 24, 'bold'), bg='powder blue',
                               text='Hotel Management System', fg='slate blue', padx=2, pady=8)
        self.lbl_title.pack()

        # Widgets

        # Customer reference
        self.lbl_customer_ref = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Customer Ref:',
                                      padx=2)
        self.lbl_customer_ref.grid(row=0, column=0, sticky=W)
        self.txt_customer_ref = Entry(leftframe, font=('calibry', 12), width=20, textvariable=customer_ref)
        self.txt_customer_ref.grid(row=0, column=1, pady=3, padx=20)

        # First Name
        self.lbl_first_name = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='First Name:',
                                    padx=2)
        self.lbl_first_name.grid(row=1, column=0, sticky=W)
        self.txt_first_name = Entry(leftframe, font=('calibry', 12), width=20, textvariable=first_name)
        self.txt_first_name.grid(row=1, column=1, pady=3, padx=20)

        # Last Name
        self.lbl_last_name = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Last Name:', padx=2)
        self.lbl_last_name.grid(row=2, column=0, sticky=W)
        self.txt_last_name = Entry(leftframe, font=('calibry', 12), width=20, textvariable=last_name)
        self.txt_last_name.grid(row=2, column=1, pady=3, padx=20)

        # Address
        self.lbl_address = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Address:', padx=2)
        self.lbl_address.grid(row=3, column=0, sticky=W)
        self.txt_address = Entry(leftframe, font=('calibry', 12), width=20, textvariable=address)
        self.txt_address.grid(row=3, column=1, pady=3, padx=20)

        # Pin Code
        self.lbl_pin_code = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='PIN code:', padx=2)
        self.lbl_pin_code.grid(row=4, column=0, sticky=W)
        self.txt_pin_code = Entry(leftframe, font=('calibry', 12), width=20, textvariable=pin_code)
        self.txt_pin_code.grid(row=4, column=1, pady=3, padx=20)

        # Mobile Number
        self.lbl_mobile = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Mobile:', padx=2)
        self.lbl_mobile.grid(row=5, column=0, sticky=W)
        self.txt_mobile = Entry(leftframe, font=('calibry', 12), width=20, textvariable=mobile)
        self.txt_mobile.grid(row=5, column=1, pady=3, padx=20)

        # Email id
        self.lbl_email = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Email id:', padx=2)
        self.lbl_email.grid(row=6, column=0, sticky=W)
        self.txt_email = Entry(leftframe, font=('calibry', 12), width=20, textvariable=email)
        self.txt_email.grid(row=6, column=1, pady=3, padx=20)

        # Nationality
        self.lbl_nationality = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Nationality:',
                                     padx=2)
        self.lbl_nationality.grid(row=7, column=0, sticky=W)
        self.cbo_nationality = ttk.Combobox(leftframe, textvariable=nationality, font=('calibry', 12),
                                            state='readonly', width=18)
        self.cbo_nationality['value'] = ('', 'India', 'British', 'Nigeria', 'Kenya', 'Iraq', 'Morocco', 'Canada',
                                         'France', 'Other')
        self.cbo_nationality.current(0)
        self.cbo_nationality.grid(row=7, column=1, pady=3, padx=20)

        # Date of birth
        self.lbl_dob = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Date of birth:', padx=2)
        self.lbl_dob.grid(row=8, column=0, sticky=W)
        self.txt_dob = Entry(leftframe, font=('calibry', 12), width=20, textvariable=date_of_birth)
        self.txt_dob.grid(row=8, column=1, pady=3, padx=20)

        # Identity
        self.lbl_identity = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Identity proof:',
                                  padx=2)
        self.lbl_identity.grid(row=9, column=0, sticky=W)
        self.cbo_identity = ttk.Combobox(leftframe, textvariable=identity, font=('calibry', 12), state='readonly',
                                         width=18)
        self.cbo_identity['value'] = ('', 'Passport', 'Pan Card', 'Aadhar card', 'Voter ID', 'Driving License')
        self.cbo_identity.current(0)
        self.cbo_identity.grid(row=9, column=1, pady=3, padx=20)

        # Gender
        self.lbl_gender = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Gender:', padx=2)
        self.lbl_gender.grid(row=10, column=0, sticky=W)
        self.cbo_gender = ttk.Combobox(leftframe, font=('calibry', 12), textvariable=gender, state='readonly', width=18)
        self.cbo_gender['value'] = ('', 'Male', 'Female', 'Other')
        self.cbo_gender.current(0)
        self.cbo_gender.grid(row=10, column=1, pady=3, padx=20)

        # Check in Date
        self.lbl_check_in_date = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Check in date:',
                                       padx=2)
        self.lbl_check_in_date.grid(row=11, column=0, sticky=W)
        self.txt_check_in_date = Entry(leftframe, font=('calibry', 12), width=20, textvariable=check_in_date)
        self.txt_check_in_date.grid(row=11, column=1, pady=3, padx=20)

        # Check out Date
        self.lbl_check_out_date = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue',
                                        text='Check out date:', padx=2)
        self.lbl_check_out_date.grid(row=12, column=0, sticky=W)
        self.txt_check_out_date = Entry(leftframe, font=('calibry', 12), width=20, textvariable=check_out_date)
        self.txt_check_out_date.grid(row=12, column=1, pady=3, padx=20)

        # Meal
        self.lbl_meal = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Meal:', padx=2)
        self.lbl_meal.grid(row=13, column=0, sticky=W)
        self.cbo_meal = ttk.Combobox(leftframe, font=('calibry', 12), textvariable=meal, state='readonly', width=18)
        self.cbo_meal['value'] = ('', 'Breakfast', 'Lunch', 'Dinner')
        self.cbo_meal.current(0)
        self.cbo_meal.grid(row=13, column=1, pady=3, padx=20)

        # Room type
        self.lbl_room_type = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Room type:', padx=2)
        self.lbl_room_type.grid(row=14, column=0, sticky=W)
        self.cbo_room_type = ttk.Combobox(leftframe, font=('calibry', 12), textvariable=room_type, state='readonly',
                                          width=18)
        self.cbo_room_type['value'] = ('', 'Single', 'Double', 'Family')
        self.cbo_room_type.current(0)
        self.cbo_room_type.grid(row=14, column=1, pady=3, padx=20)

        # Room number
        self.lbl_room_no = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Room Number:', padx=2)
        self.lbl_room_no.grid(row=15, column=0, sticky=W)
        self.cbo_room_no = ttk.Combobox(leftframe, font=('calibry', 12), textvariable=room_no, state='readonly',
                                        width=18)
        self.cbo_room_no['value'] = ('', '001', '002', '003', '004', '005', '006')
        self.cbo_room_no.current(0)
        self.cbo_room_no.grid(row=15, column=1, pady=3, padx=20)

        # Room ext number
        self.lbl_room_ext_no = Label(leftframe, font=('calibry', 12, 'bold'), bg='powder blue', text='Room Ext. No:',
                                     padx=2)
        self.lbl_room_ext_no.grid(row=16, column=0, sticky=W)
        self.cbo_room_ext_no = ttk.Combobox(leftframe, font=('calibry', 12), textvariable=room_ext_no, state='readonly',
                                            width=18)
        self.cbo_room_ext_no['value'] = ('', '101', '102', '201', '202', '301', '302')
        self.cbo_room_ext_no.current(0)
        self.cbo_room_ext_no.grid(row=16, column=1, pady=3, padx=20)

        # Receipt
        self.lbl_receipt = Label(rightframe, font=('arial', 16, 'bold'),
                                 text='RECEIPT', pady=10, bg='cadet blue', bd=5)
        self.lbl_receipt.grid(row=0, column=0, columnspan=17, padx=1, sticky=N)
        self.txt_receipt = Text(rightframe, height=15, width=132, font=('calibry', 10, 'bold'), pady=10, padx=2, bd=5)
        self.txt_receipt.grid(row=1, column=0, columnspan=2)

        # Payment
        self.lbl_days = Label(rightframe, font=('calibry', 12, 'bold'), text='No. of Days:', bd=7, bg='cadet blue',
                              pady=1)
        self.lbl_days.grid(row=2, column=0, sticky=W)
        self.txt_days = Entry(rightframe, font=('calibry', 12, 'bold'), width=87, bd=3, textvariable=no_of_days,
                              justify=LEFT)
        self.txt_days.grid(row=2, column=1)

        self.lbl_tax_paid = Label(rightframe, font=('calibry', 12, 'bold'), text='Tax Paid ₹:', bd=7, bg='cadet blue',
                                  pady=1)
        self.lbl_tax_paid.grid(row=3, column=0, sticky=W)
        self.txt_tax_paid = Entry(rightframe, font=('calibry', 12, 'bold'), width=87, bd=3, textvariable=tax_paid,
                                  justify=LEFT)
        self.txt_tax_paid.grid(row=3, column=1)

        self.lbl_sub_total = Label(rightframe, font=('calibry', 12, 'bold'), text='Sub Total ₹:', bd=7, bg='cadet blue',
                                   pady=1)
        self.lbl_sub_total.grid(row=4, column=0, sticky=W)
        self.txt_sub_total = Entry(rightframe, font=('calibry', 12, 'bold'), width=87, bd=3, textvariable=sub_total,
                                   justify=LEFT)
        self.txt_sub_total.grid(row=4, column=1)

        self.lbl_total_cost = Label(rightframe, font=('calibry', 12, 'bold'), text='Total Cost ₹:', bd=7, bg='cadet blue',
                                    pady=1)
        self.lbl_total_cost.grid(row=5, column=0, sticky=W)
        self.txt_total_cost = Entry(rightframe, font=('calibry', 12, 'bold'), width=87, bd=3, textvariable=total_cost,
                                    justify=LEFT)
        self.txt_total_cost.grid(row=5, column=1)

        self.lbl_money_paid_by = Label(rightframe, font=('calibry', 12, 'bold'), text='Money Paid by:', bd=7,
                                       bg='cadet blue', pady=1)
        self.lbl_money_paid_by.grid(row=6, column=0, sticky=W)
        self.cbo_money_paid_by = ttk.Combobox(rightframe, font=('calibry', 12, 'bold'), width=85,
                                              textvariable=money_paid_by, state='readonly')
        self.cbo_money_paid_by['value'] = ('', 'Cash', 'Check', 'Online')
        self.cbo_money_paid_by.current(0)
        self.cbo_money_paid_by.grid(row=6, column=1)

        # Buttons
        self.btn_total = Button(bottomframe, text='Total', font=('calibry', 16, 'bold'), bd=6, pady=10, padx=5,
                                bg='cadet blue', width=23, command=total_cost_and_days)
        self.btn_total.grid(row=0, column=0, padx=4, pady=16)

        self.btn_receipt = Button(bottomframe, text='Receipt', font=('calibry', 16, 'bold'), bd=6, pady=10, padx=5,
                                  bg='cadet blue', width=23, command=receipt)
        self.btn_receipt.grid(row=0, column=2, padx=4, pady=16)

        self.btn_reset = Button(bottomframe, text='Reset', font=('calibry', 16, 'bold'), bd=6, pady=10, padx=5,
                                bg='cadet blue', width=23, command=reset)
        self.btn_reset.grid(row=0, column=4, padx=4, pady=16)

        self.btn_exit = Button(bottomframe, text='Exit', font=('calibry', 16, 'bold'), bd=6, pady=10, padx=5,
                               bg='cadet blue', width=23, command=i_exit)
        self.btn_exit.grid(row=0, column=6, padx=4, pady=16)

        # Menu Bar
        self.menubar = Menu(master)
        master.config(menu=self.menubar)
        self.filemenu = Menu(self.menubar, tearoff=0, activeborderwidth=5)
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='New', command=reset)
        self.filemenu.add_command(label='Save', command=save_receipt)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=i_exit)


if __name__ == '__main__':
    root = Tk()
    application = Hotel(root)
    root.mainloop()
