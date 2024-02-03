import pyperclip
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.font as tkFont


root = ThemedTk(theme='black')
root.title("Sp.d.calc")
root.attributes('-topmost', True)
root.wm_attributes('-alpha', 0.9)
root.geometry('250x200')
root.resizable(width=False, height=False)


mainframe = ttk.Frame(root)
mainframe.place(relx=0, rely=0, relwidth=1, relheight=1)
bottomframe = ttk.Frame(root)
bottomframe.place(relx=0, rely=0.65, relwidth=1, relheight=0.5)


def paste_degree():
    _input_degree = pyperclip.paste()
    try:
        value = float(_input_degree)  # Попытка преобразовать строку в число с плавающей точкой
        input_degree.set(str(value))
        calculate_degree()
        title.config(text="Enter your degree")
    except ValueError:  # Если преобразование не удалось и было вызвано исключение ValueError
        title.config(text="This is NOT a number!")


def calculate_degree():
    root.after(1000, calculate_degree)
    if old_input_degree.get() != input_degree.get():
        try:
            value = float(input_degree.get())
            if value > 0:
                calculated_degree.set(str(180 - value))
            else:
                calculated_degree.set(str(180 + value))
            old_input_degree.set(input_degree.get())
            pyperclip.copy(calculated_degree.get())
        except ValueError:
            pass


title = ttk.Label(mainframe, text="Enter your degree", font=30)
btn_calc_degree = ttk.Button(mainframe, text="paste", command=paste_degree)
input_degree = StringVar()
old_input_degree = StringVar()
calculated_degree = StringVar()
input_degree_entry = ttk.Entry(mainframe, width=14, textvariable=input_degree)
output_degree = ttk.Entry(bottomframe, width=14, textvariable=calculated_degree)
label_calc_degree = ttk.Label(bottomframe, text="Calculated degree:", font=30)


title.pack()
input_degree_entry.pack()
btn_calc_degree.pack(padx=10, pady=10)
btn_calc_degree.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.3)

btn_style = ttk.Style()
font_style = tkFont.Font(family="Arial", size=14, weight="bold")
style = ttk.Style()
style.configure("TButton", font=font_style, anchor="center")
label_calc_degree.pack()
output_degree.pack()


input_degree_entry.focus()
root.bind("<Return>", calculate_degree)
root.after(1000, calculate_degree)


root.mainloop()
