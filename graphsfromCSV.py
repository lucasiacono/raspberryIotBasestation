import matplotlib.pyplot as plt
import csv
import numpy as np

data = csv.reader(open('C:\Users\LAPIC\Google Drive\Dato2.csv'), delimiter=',')
data.next() # do not read header

hora = []
temp = [] 


for col in data:
    hora.append ("%02d" % int(str(col[1])+"%02d" % int(str(col[2]))+"%02d" % int (str(col[3]))))
    temp.append(float(col[7]))
    lucas= plt.plot(hora,temp)
    plt.savefig('C:\Users\LAPIC\Desktop\Dato2.jpg', dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)












