import tkinter
from tkinter import ttk

wdw = tkinter.Tk()
wdw.configure(bg='lightblue', border=10)

wdw.columnconfigure(0, weight=1)
wdw.columnconfigure(1, weight=3)

etiqueta = ttk.Label(wdw, text='Lista de la compra', background='lightblue', font=('Helvetica', 12, 'bold'))
etiqueta.grid(row=0, column=0, sticky=tkinter.W, pady=10, padx=10)

lista =['pan', 'leche', 'cerveza', 'papel de cocina', 'mangos', 'aguacates']
lista_items = tkinter.StringVar(value=lista)

l = tkinter.Listbox(wdw, height=15, width=25, listvariable=lista_items, bg='lightyellow', fg='black', font=('ariel',10))
l.grid(column=0, row=2, sticky=tkinter.W, pady=5, padx=5)

wdw.mainloop()