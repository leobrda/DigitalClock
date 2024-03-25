from time import strftime
from tkinter import *
from openpyxl.chart import label

root = Tk()
root.title('Relógio')


def relogio():
    horario = strftime('%H:%M:%S')
    label.config(text=horario)
    label.after(1000, relogio)


label = Label(root, font=('Helvetica', 60), background='#000', foreground='#00FF04')
label.pack(anchor='center')

relogio()
mainloop()


