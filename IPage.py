# -*- Coding: UTF-8 -*-
# Python 3
#                     ██╗██████╗  █████╗  ██████╗ ███████╗
#                     ██║██╔══██╗██╔══██╗██╔════╝ ██╔════╝
#                     ██║██████╔╝███████║██║  ███╗█████╗  
#                     ██║██╔═══╝ ██╔══██║██║   ██║██╔══╝  
#                     ██║██║     ██║  ██║╚██████╔╝███████╗
#                     ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
#                                                         By: LawlietJH
#                                                               v1.0.4

import sys
import os



Version = "v1.0.4"



#=======================================================================



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
	
	os.system("cls && Title IPage.py                " + \
			"By: LawlietJH                " + Version + "    ")
	
	print("\n\n\n", Banner1, "\n\n\n", Autor, "\n\n\n{:^80}\n\n".format(Version))
	
	try: os.system("TimeOut /NoBreak 2 > Nul")
	except: Dat()



#=======================================================================



def Salir(Num=0):	# Fucnión Que Permite Salir Del Script Sin Error Alguno.
	
	try:
		time.sleep(1.5)
		exit(Num)
	except KeyboardInterrupt:
		Salir(Num)



#~ Función Que Permite Esconder El Cursor de la Pantalla (La rayita que parpadea xD).
def HiddenCursor(imp="Hide"):
	
	#~ imp = imp.title()		#Devuelve la cadena solo con la primera letra de cada palabra en mayuscula
	imp = imp.capitalize()		#Devuelve la cadena solo con la primera letra de la primer palabra en mayuscula

	if os.name == 'nt':
		import msvcrt
		import ctypes

		class _CursorInfo(ctypes.Structure):
			_fields_ = [("size", ctypes.c_int),
						("visible", ctypes.c_byte)]
	
	def hide_cursor():
		if os.name == 'nt':
			ci = _CursorInfo()
			handle = ctypes.windll.kernel32.GetStdHandle(-11)
			ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
			ci.visible = False
			ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
		elif os.name == 'posix':
			sys.stdout.write("\033[?25l")
			sys.stdout.flush()

	def show_cursor():
		if os.name == 'nt':
			ci = _CursorInfo()
			handle = ctypes.windll.kernel32.GetStdHandle(-11)
			ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
			ci.visible = True
			ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
		elif os.name == 'posix':
			sys.stdout.write("\033[?25h")
			sys.stdout.flush()
			
	if imp == "Hide":
		hide_cursor()
	elif imp =="Show":
		show_cursor()
	else:
		pass



#=======================================================================



def getIP(Pagina): # Función que obtiene la IP de una Página Web solicitada.
	
	global IPvX
	
	IPvX = "4"
	
	if Pagina == "": return True
	
	Cadena = os.popen("ping -n 1 " + Pagina).read()
	
	try:
		
		IP = Cadena.split("[")[1].split("]")[0]
		
		if ":" in IP: IPvX = "6"
		
		return IP
		
	except IndexError: return False



def Main(): # Función Principal. Manda a Llamra Los Métodos Necesarios.
	
	Pagina = input("\n\n    [+] Página Web: ")
	
	IP = getIP(Pagina)
	
	if IP == True: print("\n\t [!] Escribe Una Página Web. \n\t [*] Ejemplo: www.google.com  o  google.com")
	elif IP == False: print("\n\t [!] Página Inexistente! \n\t [*] Ejemplo: www.google.com  o  google.com")
	else:
		
		if IPvX == "4": print("\n\t [*]  IPv4  : " + IP)
		elif IPvX == "6": print("\n\t [*]  IPv6  : " + IP)



#=======================================================================



# Todo Lo Que Este Dentro De Esta Condicion Será Ejecutado Solo Si El Script Se Ejecuta Directamente.
# Esto nos permite Poder llamar las funciones desde otro escript sin ejecutar los comandos dentro del condicional.
if __name__ == "__main__":  
	
	IPvX = "4"
	
	os.system("Title IPage.py                " + \
	"By: LawlietJH                " + Version + "    ")
	
	HiddenCursor()
	
	while True:
		
		try:
			Main()
		except KeyboardInterrupt:
			
			Dat()
			break


