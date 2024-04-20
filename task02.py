from tkinter import *
from math import *
import re
def add_digit(digit):
    value = calc.get()+str(digit)
    calc.delete(0, END)
    calc.insert(0, value)
    
def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    calc.delete(0, END)
    calc.insert(0, value+operation)

def clear():
    calc.delete(0, END)
    calc.insert(0,'')

def create_digit_button(digit):
    return Button(text=digit, bd=5, font=('Arial', 13),  command=lambda : add_digit(digit))

def create_operation_button(operation):

    return Button(text=operation, bd=5, font=('Arial', 13),  command=lambda : add_operation(operation))

def create_clear_button(operation):
    return Button(text=operation, bd=5, font=('Arial', 13),  command=lambda :clear())

def calculate():
     value = calc.get()
     if ('%' in value):
         nums = re.findall(r'\d+', value)
         c=int(nums[0])/int(nums[1])*100
         calc.delete(0, END)
         calc.insert(0, str(c))
     else:
         calc.delete(0, END)
         calc.insert(0, eval(value))

def make_calc(operation):
    return Button(text=operation, bd=5, font=('Arial', 13),   command =lambda :calculate())

def operation_sin(operation):
    value = eval(calc.get())
    calc.delete(0, END)
    calc.insert(0, sin(float(value)))

def operation_cos(operation):
    value = eval(calc.get())
    calc.delete(0, END)
    calc.insert(0, cos(float(value)))

def operation_tan(operation):
    value = eval(calc.get())
    calc.delete(0, END)
    calc.insert(0, tan(float(value)))

def operation_ctg(operation):
    value = eval(calc.get())
    calc.delete(0, END)
    calc.insert(0, 1/tan(float(value)))

def operation_lg(operation):
    value = eval(calc.get())
    calc.delete(0, END)
    calc.insert(0, log10(float(value)))

def operation_ln(operation):
    value = eval(calc.get())
    calc.delete(0, END)
    calc.insert(0, log(float(value)))


def operation_01(operation):
    value = eval(calc.get())
    b=''
    n=int(value)
    while n> 0:
        b = str(n % 2) + b
        n = n // 2
    calc.delete(0, END)
    calc.insert(0, b)

root = Tk()
root['bg']='#fafafa'
root.title('Калькулятор')
root.wm_attributes('-alpha')
root.geometry('300x315')

calc = Entry(root, font=('Arial',15), justify=RIGHT)
calc.grid(row=0, column=0, columnspan=6, stick='we')

create_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
create_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
create_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
create_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
create_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
create_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
create_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
create_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
create_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
create_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)
create_digit_button('.').grid(row=5, column=0, stick='wens', padx=5, pady=5)
create_digit_button('%').grid(row=5, column=3, stick='wens', padx=5, pady=5)

create_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
create_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
create_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
create_operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

Button(text='Sin', bd=5, font=('Arial', 13),  command=lambda : operation_sin('Son')).grid(row=1, column=4, stick='wens', padx=5, pady=5)
Button(text='Cos', bd=5, font=('Arial', 13),  command=lambda : operation_cos('Cis')).grid(row=2, column=4, stick='wens', padx=5, pady=5)
Button(text='Tan', bd=5, font=('Arial', 13),  command=lambda : operation_tan('Tan')).grid(row=3, column=4, stick='wens', padx=5, pady=5)
Button(text='Ctg', bd=5, font=('Arial', 13),  command=lambda : operation_ctg('Ctg')).grid(row=4, column=4, stick='wens', padx=5, pady=5)
Button(text='Lg', bd=5, font=('Arial', 13),  command=lambda : operation_lg('Log')).grid(row=5, column=1, stick='wens', padx=5, pady=5)
Button(text='ln', bd=5, font=('Arial', 13),  command=lambda : operation_ln('ln')).grid(row=5, column=2, stick='wens', padx=5, pady=5)
Button(text='01', bd=5, font=('Arial', 13),  command=lambda : operation_01('01')).grid(row=5, column=4, stick='wens', padx=5, pady=5)


make_calc('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
create_clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

for i in range(4):
    root.grid_columnconfigure(i, minsize=60)

for i in range(1,5):
    root.grid_rowconfigure(i, minsize=60)

root.mainloop()
