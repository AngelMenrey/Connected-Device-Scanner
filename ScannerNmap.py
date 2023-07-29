
#Author: Angel Emanuel Mendoza Reyes
import nmap
scanner = nmap.PortScanner()
#Ingrese su IP a escaner en formato barra diagonal 
ip = input("Ingrese una direccion IP para realizar el escaneo")
print("La IP ingresada es: ", ip)
scanner.scan(ip)
print(scanner.all_hosts())