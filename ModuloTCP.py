'''
Created on 03/01/2013

@author: lapic
'''
# -*- coding: utf-8 -*-
import socket
import serial
import time
import datetime

s=socket.socket()
s.connect(("172.22.72.1",4000))

serie = serial.Serial("COM9", 9600)
#serie.timeout=1;
fin = 0
entrada = 3
pos = 0

while not(fin):
    time.sleep(0.5)
    dataLen = serie.inWaiting()
    now = datetime.datetime.now()
    micro = now.microsecond
    data = serie.read(dataLen)
    data_inicio = data[0:1].encode("hex")
    if data_inicio != 0 :
        #print entrada
        addr1 = "403a3c17"
        addr2 = "4032e051"
        addr3 = "403a3c2a"
        addr4 = "403a3d0e"
        byte_addr = data[9:13].encode("hex")  #captura la direccion del nodo
       
        if addr2 == byte_addr:#testea si la direccion es la del nodo2
            print "Nodo 2"
            dato = [2,0,0,0]
            print dato
            hora = datetime.datetime.now()
            print "Fecha y hora:", hora
            dato = [2,hora,0,0]
            print dato
            for i in range(dataLen):
                    byte = data[i].encode("hex")
    
                    if byte == "7e":
                            byte_1 = data[i+3].encode("hex")
    
                            if byte_1 == "90":
    
                                comienzo = "7e00"
                                data_inicio = data[i:i+2].encode("hex")
                                direccion = data[i+9:i+13].encode("hex")
                                if data_inicio == comienzo:
    
                                    temp_e = data[i+16].encode("hex")
                                    #print "temp_e:", temp_e
                                    #s.send("temp_e: ")
                                    #s.send(str(temp_e))
                                    #s.send("\n")
                                    temp_d = data[i+17].encode("hex")
                                    hum_e = data[i+18].encode("hex")
                                    hum_d = data[i+19].encode("hex")
    
                                    if temp_e == "7d":
                                        pos = pos +1
                                    #    print "entro1"
                                    #    s.send("entro1")
                                    #    s.send("\n")
                                        temp_e = data[i+16+pos].encode("hex")
                                        temp_e = int(temp_e,16)
                                    #    print "temp_e:", temp_e
                                    #    s.send("temp_e: ")
                                    #    s.send(str(temp_e))
                                    #    s.send("\n")
                                        xtemp = (temp_e  ^ 0x20)
                                        temp_d = data[i+17+pos].encode("hex")
    
                                        hum_e = data[i+18+pos].encode("hex")
                                        hum_d = data[i+19+pos].encode("hex")
                                    #    print "temp_d:", temp_d
                                    #    s.send("temp_d: ")
                                    #    s.send(str(temp_d))
                                    #    s.send("\n")
    
                                    elif temp_e != "7d":
                                        xtemp = int(temp_e,16)
    
                                    if temp_d == "7d":
                                        pos = pos +1
                                        temp_d = data[i+17+pos].encode("hex")
                                        temp_d = int(temp_d,16)
                                        ytemp = (temp_d ^ 0x20)* 0.01
    
                                        hum_e = data[i+18+pos].encode("hex")
                                        hum_d = data[i+19+pos].encode("hex")
    
                                    elif temp_d != "7d":
                                        ytemp = int(temp_d,16)* 0.01
    
                                    if hum_e == "7d":
                                        pos=pos+1
                                        hum_e = data[i+18+pos].encode("hex")
                                        hum_e = int(hum_e,16)
                                        xhum = (hum_e ^ 0x20)
                                        hum_d = data[i+19+pos].encode("hex")
    
                                    elif hum_e != "7d":
                                        xhum = int(hum_e,16)
    
                                    if hum_d == "7d":
                                        pos=pos+1
                                        hum_d = data[i+19+pos].encode("hex")
                                        hum_d = int(hum_d,16)
                                        yhum = (hum_d ^ 0x20)* 0.01
    
                                    elif hum_d != "7d":
                                        yhum = int(hum_d, 16)* 0.01
    
                                    sumt = str(xtemp + ytemp)
                                    print "temperatura:", sumt
                                    dato = [2,hora,sumt,0]
                                    print dato
                                        
                                    sumh = str(xhum + yhum)
                                    print "humedad:", sumh
                                    dato = [2,hora,sumt,sumh]
                                    print dato
                                    s.send(dato)
                                    
            data = 0
            serie.flushInput()
            serie.flush()
          
s.close()
