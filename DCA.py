from tkinter import *
from dca_fix import *
from tkinter import messagebox

def calculate_all():
    ans_rate  = arps_rate(float(e2.get()),float(e3.get()),float(e4.get()),float(e6.get()))
    box_1.delete(0,END)
    box_1.insert(0, ans_rate)
    ans_cum_t = cumprod_time(float(e2.get()),float(e3.get()),float(e4.get()), float(e6.get()), e1.get())
    box_2.delete(0, END)
    box_2.insert(0, ans_cum_t)
    ans_cum_lt= cumprod_limit(float(e2.get()), float(e3.get()), float(e4.get()), float(e5.get()), e1.get())
    box_3.delete(0, END)
    box_3.insert(0, ans_cum_lt)
    ans_lt    = duration(float(e2.get()), float(e3.get()),float(e4.get()),float(e5.get()))
    box_4.delete(0, END)
    box_4.insert(0, ans_lt)

def showMsg():
    messagebox.showinfo('Message', (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()))

window = Tk()
window.wm_title("Simple Decline Curve Analysis")

#label
Label (window, text = "Simple Decline Curve Analysis using Arps Formula", bg= 'black', fg = 'white'). grid(row=0, column = 1,columnspan = 15, sticky = W)

#listbox

#label input
l1 = Label (window, text = "Fluids")
l1.grid(row=1, column=0)

l2 = Label (window, text = "Initial Rate(MScfd / BOPD)")
l2.grid(row=2, column=0)

l3 = Label (window, text = "Di Factor")
l3.grid(row=3, column=0)

l4 = Label (window, text = "b Factor")
l4.grid(row=4, column=0)

l5 = Label (window, text = "Economic Limit Rate (MScfd / BOPD)")
l5.grid(row=5, column=0)

l6 = Label (window, text = "Desired Duration (Days)")
l6.grid(row=6, column=0)

#label output
l11 = Label(window, text="Arps Rate")
l11.grid(row=1, column=2)

l12 = Label(window, text="Arps Cumulative Production ")
l12.grid(row=2, column=2)

l13 = Label(window, text="Cumulative Production at Lifetime")
l13.grid(row=3, column=2)

l14 = Label(window, text="Lifetime")
l14.grid(row=4, column=2)



#Input value
fluids_in = StringVar()
e1 = Entry (window)
e1.grid(row=1, column = 1)

qi_in = DoubleVar()
e2 = Entry (window, textvariable = qi_in)
e2.grid(row=2, column = 1)

di_factor_in = DoubleVar()
e3 = Entry (window, textvariable = di_factor_in)
e3.grid(row=3, column = 1)

b_factor_in = DoubleVar()
e4 = Entry (window, textvariable = b_factor_in)
e4.grid(row=4, column = 1)

q_ecl_in = DoubleVar()
e5 = Entry (window, textvariable = q_ecl_in)
e5.grid(row=5, column = 1)

time_in = DoubleVar()
e6 = Entry (window, textvariable = time_in)
e6.grid(row=6, column = 1)

#output value
box_1 = Entry(window)
box_1.grid(row=1, column = 3)

box_2 = Entry(window)
box_2.grid(row=2, column = 3)

box_3 = Entry(window)
box_3.grid(row=3, column = 3)

box_4 = Entry(window)
box_4.grid(row=4, column = 3)

b1 = Button (window, text = "Calculate All", command = calculate_all )#, height = 10, width = 10)
b1.grid(row=1, column = 5)

b2 = Button (window, text = "Close", command = window.destroy) #, height = 10, width = 10)
b2.grid(row=2, column = 5)

#list1 = Listbox(window, height=10, width=10)
#list1.grid(row=3, column =2, columnspan=3)


window.mainloop()