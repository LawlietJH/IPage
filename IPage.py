# -*- Coding: UTF-8 -*-
# Python 3
# IPage.py

import sys
import os



Autor = "LawlietJH"
Version = "v1.0.0" 



def getIP(Pagina): # Función que obtiene la IP de una Página Web solicitada.
	
	if Pagina == "": return True
	
	Comando = "ping " + Pagina
	Cadena = os.popen(Comando)
	Cadena = Cadena.read()

	try:
		
		IP = Cadena.split("[")[1].split("]")[0]
		
		return IP
		
	except IndexError: return False



def Main():
	
	Pagina = input("\n\n\n    [+] Página Web: ")
	
	IP = getIP(Pagina)
	
	if IP == True: print("\n\t [!] Escribe Una Página Web. \n\n\t [*] Ejemplo: www.google.com  o  google.com")
	elif IP == False: print("\n\t [!] Página Inexistente! \n\n\t [*] Ejemplo: www.google.com  o  google.com")
	else: print('\n\t [*] IP de "' + Pagina + '": ' + IP)



if __name__ == "__main__":
	
	while True:
		
		Main()
