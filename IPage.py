# -*- Coding: UTF-8 -*-
# Python 3
#                    ██╗██████╗  █████╗  ██████╗ ███████╗
#                    ██║██╔══██╗██╔══██╗██╔════╝ ██╔════╝
#                    ██║██████╔╝███████║██║  ███╗█████╗  
#                    ██║██╔═══╝ ██╔══██║██║   ██║██╔══╝  
#                    ██║██║     ██║  ██║╚██████╔╝███████╗
#                    ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
#                                                         By: LawlietJH
#                                                               v1.0.2

import sys
import os



Version = "v1.0.2"



# Banners: http://patorjk.com/software/taag/



Banner1 = """
                     ██╗██████╗  █████╗  ██████╗ ███████╗
                     ██║██╔══██╗██╔══██╗██╔════╝ ██╔════╝
                     ██║██████╔╝███████║██║  ███╗█████╗  
                     ██║██╔═══╝ ██╔══██║██║   ██║██╔══╝  
                     ██║██║     ██║  ██║╚██████╔╝███████╗
                     ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
"""
# Fuente: ANSI Shadow - http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=IPage



Banner2 = """
                                 ╦╔═╗┌─┐┌─┐┌─┐
                                 ║╠═╝├─┤│ ┬├┤ 
                                 ╩╩  ┴ ┴└─┘└─┘
"""
# Fuente: Calvin S - http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=IPage



Autor = """
                            ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
                            ║  ├─┤││││  │├┤  │ ║╠═╣
                            ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩
"""
# Fuente: Calvin S - http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=LawlietJH



#=======================================================================



def Dat():	# Función Que Permite Mostrar Los Datos Del Script.
	
	os.system("cls && Title IPage.py                "+\
			"By: LawlietJH                "+Version+"    ")
	
	print("\n\n\n", Banner1, "\n\n\n", Autor, "\n\n\n{:^80}\n\n".format(Version))
	
	try:
		os.system("TimeOut /NoBreak 2 > Nul")
	except:
		Dat()



#=======================================================================



def getIP(Pagina): # Función que obtiene la IP de una Página Web solicitada.
	
	if Pagina == "": return True
	
	Cadena = os.popen("ping -n 1 " + Pagina).read()
	
	try:
		
		IP = Cadena.split("[")[1].split("]")[0]
		
		return IP
		
	except IndexError: return False



def Main(): # Función Principal. Manda a Llamra Los Métodos Necesarios.
	
	Pagina = input("\n\n\n    [+] Página Web: ")
	
	IP = getIP(Pagina)
	
	if IP == True: print("\n\t [!] Escribe Una Página Web. \n\t [*] Ejemplo: www.google.com  o  google.com")
	elif IP == False: print("\n\t [!] Página Inexistente! \n\t [*] Ejemplo: www.google.com  o  google.com")
	else: print("\n\t [*]  IP  : " + IP)



#=======================================================================



# Todo Lo Que Este Dentro De Esta Condicion Será Ejecutado Solo Si El Script Se Ejecuta Directamente.
# Esto nos permite Poder llamar las funciones desde otro escript sin ejecutar los comandos dentro del condicional.
if __name__ == "__main__":  
	
	os.system("Title IPage.py                "+\
	"By: LawlietJH                "+Version+"    ")
	
	while True:
		
		try:
			Main()
		except KeyboardInterrupt:
			
			Dat()
			break


