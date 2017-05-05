# -*- Coding: UTF-8 -*-
# Python 3
#                     ██╗██████╗  █████╗  ██████╗ ███████╗
#                     ██║██╔══██╗██╔══██╗██╔════╝ ██╔════╝
#                     ██║██████╔╝███████║██║  ███╗█████╗  
#                     ██║██╔═══╝ ██╔══██║██║   ██║██╔══╝  
#                     ██║██║     ██║  ██║╚██████╔╝███████╗
#                     ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
#                                                         By: LawlietJH
#                                                         GUI - v1.0.1

from tkinter import *
import sys
import os



Version = "v1.0.1"



#=======================================================================



def getIP(): # Función que obtiene la IP de una Página Web solicitada.
	
	Pagina = Texto1.get()
	
	if Pagina == "":
		
		Et5.config(text="Escribe Una Página Web.")
		
		return
	
	Cadena = os.popen("ping -n 1 " + Pagina).read()
	
	try:
		
		IP = Cadena.split("[")[1].split("]")[0]
		
		Et5.config(text=IP)
		
	except IndexError: Et5.config(text="Página Inexistente!")



#=======================================================================



if __name__ == "__main__":
	
	root = Tk()
	
	root.title("GUIPage.pyw    By: LawlietJH    " + Version)
	root.geometry("+240+160")
	
	#===============================================================
	
	# Ventana Principal
	Fr = Frame(root)
	Fr.grid(column=0, row=0, padx=(20,30), pady=(20,30))
	Fr.columnconfigure(0, weight=1)
	Fr.rowconfigure(0, weight=1)
	
	#===============================================================
	
	# Etiqueta 1:
	Et1 = Label(Fr, text="Ejemplo: ")
	Et1.grid(row=0, column=0, sticky=E)
	
	# Etiqueta 2:
	Et2 = Label(Fr, text="www.google.com  o  google.com")
	Et2.grid(row=0, column=1, sticky=W)
	
	#===============================================================
	
	# Etiqueta 3:
	Et3 = Label(Fr, text="Página: ")
	Et3.grid(row=1, column=0, sticky=E)
	
	# Cuadro de Texto 1:
	Texto1 = Entry(Fr, width=30)
	Texto1.grid(row=1, column=1)
	
	# Boton 1:
	BgetIP = Button(Fr, fg="Blue", text=" IP ", command=getIP)
	BgetIP.grid(row=1, column=2)
	
	#===============================================================
	
	# Etiqueta 4:
	Et4 = Label(Fr, text="IP: ")
	Et4.grid(row=3, column=0, sticky=E)
	
	# Etiqueta 5:
	Et5 = Label(Fr, text="")
	Et5.grid(row=3, column=1, sticky=W)
	
	
	#===============================================================
	
	
	root.mainloop()



#=======================================================================


