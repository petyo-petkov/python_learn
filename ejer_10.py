import tkinter
from tkinter import ttk

wdw  = tkinter.Tk()
wdw.geometry('200x200')
wdw.title('Mi Ventana')

wdw.columnconfigure(0, weight=1)
wdw.columnconfigure(1, weight=3)

frame = tkinter.LabelFrame(height=300, width=200, text='Elije una opcíon', font=('Helvetica', 8, 'bold'))
frame.grid(column=0, row=0, sticky=tkinter.N)

markado = tkinter.StringVar()

botoncito1 = ttk.Radiobutton(frame, text='Si', value=1, variable=markado, command = lambda: print('Has dicho que Si'))
botoncito2 = ttk.Radiobutton(frame, text='No', value=2, variable=markado, command = lambda:print('Has dicho que No'))
botoncito3 = ttk.Radiobutton(frame, text='No lo se', value=3, variable=markado,  command = lambda:print('No tienes ni idea'))
boton1 = ttk.Button(wdw, text='Salir', command = lambda: wdw.quit())
boton2 = ttk.Button(wdw, text='Reiniciar', command = lambda: markado.set(None))


botoncito1.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)
botoncito2.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)
botoncito3.grid(column=0, row=2, sticky=tkinter.W, padx=5, pady=5)

boton2.grid(row=1, padx=5, pady=5)
boton1.grid(row=2, padx=5, pady=5)

wdw.mainloop()

