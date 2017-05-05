from tkinter import *
import sys
import os



def getIP(): # Función que obtiene la IP de una Página Web solicitada.
	
	Pagina = Texto1.get()
	
	if Pagina == "":
		
		Et2.config(text=" [ ! ] Escribe Una Página Web.")
		
		return
	
	Cadena = os.popen("ping -n 1 " + Pagina).read()
	
	try:
		
		IP = Cadena.split("[")[1].split("]")[0]
		
		Et2.config(text=" [+] IP: "+IP)
		
	except IndexError: Et2.config(text=" [ ! ] Página Inexistente!")



Tk = Tk()
Tk.title("GUIPage.py    By: LawlietJH    v1.0.0")
Tk.geometry("+200+150")

# Ventana Principal
Fr = Frame(Tk)
Fr.grid(column=0, row=0, padx=(20,30), pady=(20,30))
Fr.columnconfigure(0, weight=1)
Fr.rowconfigure(0, weight=1)


# Etiqueta 1:
Et1 = Label(Fr, text=" Ejemplo: www.google.com  o  google.com")
Et1.grid(column=2, row=0, sticky=W)


# Etiqueta 2:
Et2 = Label(Fr, text=" Escribe La Página Web")
Et2.grid(column=2, row=3, sticky=W)


# Boton 1:
BgetIP = Button(Fr, fg="Blue", text="  Ok!  ", command=getIP)
BgetIP.grid(column=1, row=2)


# Cuadro de Texto 1:
Texto1 = Entry(Fr, width=50)
Texto1.grid(column=2, row=2)



Tk.mainloop()


