# -*- Coding: UTF-8 -*-
# Python 3
#                     ██╗██████╗  █████╗  ██████╗ ███████╗
#                     ██║██╔══██╗██╔══██╗██╔════╝ ██╔════╝
#                     ██║██████╔╝███████║██║  ███╗█████╗  
#                     ██║██╔═══╝ ██╔══██║██║   ██║██╔══╝  
#                     ██║██║     ██║  ██║╚██████╔╝███████╗
#                     ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
#                                                         By: LawlietJH
#                                                         GUI - v1.0.4

from tkinter import *
import sys
import os



Version = "v1.0.4"



#=======================================================================



def getIP(): # Función que obtiene la IP de una Página Web solicitada.
	
	Pagina = Texto1.get()
	
	if Pagina == "":
		
		Texto2.delete(0,100)
		Texto2.insert(0,"Escribe Una Página Web.")
		
		return
	
	Cadena = os.popen("ping -n 1 " + Pagina).read()
	
	try:
		
		IP = Cadena.split("[")[1].split("]")[0]
		
		Texto2.delete(0,100)
		Texto2.insert(0,IP)
		
	except IndexError:
		Texto2.delete(0,100)
		Texto2.insert(0,"Página Inexistente!")



#=======================================================================



if __name__ == "__main__":
	
	root = Tk()
	
	root.title("IPage.py    By: LawlietJH    GUI_" + Version)
	root.iconbitmap("Imagenes\LawlietJH.ico")
	root.geometry("+320+240")
	root.resizable(0,0)
	
	#===============================================================
	
	# Ventana Principal
	Fr = Frame(root)
	Fr.grid(column=0, row=0, padx=(5,5), pady=(7,7))
	Fr.columnconfigure(0, weight=1)
	Fr.rowconfigure(0, weight=1)
	Fr.config(relief="sunken", bd=3)
	
	#===============================================================
	
	# Etiqueta 1:
	Et1 = Label(Fr, fg="Purple", text="Ejemplo: ", font="Calibri 11 bold")
	Et1.grid(row=0, column=0, sticky=E, padx=(10,0), pady=(15,5))
	
	# Etiqueta 2:
	Et2 = Label(Fr, fg="Gray", text="www.google.com  o  google.com")
	Et2.grid(row=0, column=1, sticky=(W,E), pady=(15,5))
	Et2.config(font="Calibri 10 bold italic")#, justify="center")
	
	#===============================================================
	
	# Etiqueta 3:
	Et3 = Label(Fr, fg="Purple", text="Página: ", font="Calibri 11 bold")
	Et3.grid(row=1, column=0, sticky=E)
	
	# Cuadro de Texto 1:
	Texto1 = Entry(Fr, width=30, font="Calibri 11 italic bold",\
			 justify="center", bg="White", fg="Green", bd=0,\
			 highlightbackground="#1E6FBA", highlightcolor="red",\
			 highlightthickness=1)
	Texto1.grid(row=1, column=1, sticky=W)
	Texto1.config(justify="center", state="normal")
	Texto1.insert("0","facebook.com")
	
	# Boton 1:
	BgetIP = Button(Fr, bg="cadetblue", fg="darkBlue",\
		activebackground="lightblue", activeforeground="#1E6FBA",\
		width=10, height=1, cursor="exchange", text="IP",\
		font="Calibri 10 bold", command=getIP)
	BgetIP.grid(row=1, column=2, sticky=W, padx=10)
	
	#===============================================================
	
	# Etiqueta 4:
	Et4 = Label(Fr, fg="Purple", text="IP: ", font="Calibri 11 bold")
	Et4.grid(row=3, column=0, sticky=E, pady=(5,10))
	
	# Cuadro de Texto 2:
	IP ="Esperando IP..."
	
	Texto2 = Entry(Fr, width=30, font="Calibri 11 bold", justify="center",\
			 bg="White", fg="Red", bd=0, exportselection=1,\
			 highlightbackground="#1E6FBA", highlightcolor="red",\
			 highlightthickness=1)
	Texto2.grid(row=3, column=1, sticky=W, pady=(5,10))
	Texto2.config(justify="center", state="normal")
	Texto2.insert(0, IP)
	
	
	#===============================================================
	
	
	root.mainloop()



#=======================================================================


