# -*- coding: utf-8 -*-
'''
Created on 13 oct. 2017

@author: admin
'''
import Tkinter as tk
import sqlite3


ventana = tk.Tk()

button_frame = tk.Frame(ventana)
button_frame.pack(fill=tk.X, side=tk.BOTTOM)

b1 = tk.Button(button_frame, text='Almacenar')
b2 = tk.Button(button_frame, text='Listar')
b3 = tk.Button(button_frame, text='Buscar')

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

b1.grid(row=0, column=0, sticky=tk.W+tk.E)
b2.grid(row=0, column=1, sticky=tk.W+tk.E)
b3.grid(row=0,column=2,sticky=tk.W+tk.E)
ventana.mainloop()