import socket
import ast
import csv
import time
import os, os.path

s=socket.socket()
s.bind(("172.22.72.44", 5002))
s.listen(1)
sc, addr = s.accept()
fin = False
end = False
count = 1
stop = 0
hora = []
temp = []
pilo =[]
setup = 1
while not (fin):
	existeruta = os.path.exists("Your path to setupfile:: e.g C:\Users\LAPIC\Google Drive\Sensor Cirrus\Setup.csv")	
	if existeruta == True:
	
		while not(fin):
			#time.sleep(1)
			recibido = sc.recv(102400)	
			sc.send(recibido) 
			recibidoarray = ast.literal_eval(recibido)	
			print recibidoarray 
			fila = recibidoarray
			NID = fila [0]
			with open("C:\Users\LAPIC\Google Drive\Sensor Cirrus\Dato" + str(NID) + ".csv",'ab') as fout:
				writer = csv.writer(fout)
				writer.writerow((fila [0],fila [1],fila [2],fila [3], fila [4], fila [5], fila [6], fila [7], fila [8]))
		sc.close()
		s.close()
						
	else:
		
		#time.sleep(0.1)
		valor  = os.path.getatime("C:\Users\LAPIC\Google Drive\Sensor Cirrus\Setup.csv")
		print valor
		juan = valor
		pedro = juan + count #simulo un cambio en la modificacion del archivo
		pilo.append(pedro)        
		if (pilo [count] != pilo [count-1]): #si se cumple la condicion hay que transmitir
			with open("C:\Users\LAPIC\Google Drive\Sensor Cirrus\Setup.csv") as  csvfile: 
				frecreader = csv.reader(csvfile, delimiter =',')
				for row in frecreader:
					valor = ','.join(row)
					print valor
					count = count +1
					sc.send ("Lucas")					
					sc.close()
					s.close()
