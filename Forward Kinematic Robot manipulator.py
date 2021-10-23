#library
import math
import matplotlib.pyplot as plt
import numpy as np

L1 = 1.2 #panjang lengan 1
L2 = 0.6 #panjang lengan 2

N_theta = 10 #setiap bergerak 10 kali ganti sudut sebanyak 10 degree

Thetastart=0 #sudut mulai
Thetaend=90 #sudut akhir

theta1=[]  
theta2=[]
y=[]

 #note temp itu variable untuk menampung data sementara
for i in range(Thetastart, Thetaend+1, 10): #ini +1 supaya startnya dari 1
    temp=math.radians(i)
    theta1.append(temp) #Metode append () digunakan pada akhir daftar untuk menambahkan objek baru.
    theta2.append(temp) #ini temp kita masukin supaya kita panggil tempnya yang udah di deklarasiin di atas
    y.append(i) #i ini kita panggil lagi

x0=0 #initial posisi dari sumbu x
y0=0 #initial posisi dari sumbu y

file=1 #filenya

for t1 in theta1:
    for t2 in theta2:
        x1=L1*math.cos(t1)
        y1=L1*math.sin(t1)
        x2 = x1+L2 * math.cos(t2)
        y2 = y1+L2 * math.sin(t2)

        filename=str(file)+'.jpg' #kita simpen secara string filenya dalam bentuk jpg
        file=file+1 #file jpg yang kita simpan selalu bertambah 1 dan updae setiap perpindahan sudut 10 degree

        plt.figure() #sebagai wadah tunggal yang berisi semua objek yang mewakili sumbu, grafik, teks, dan label
        plt.plot([x0, x1], [y0, y1], color='blue') # fungsi plot() untuk melakukan plotting terhadap nilai X dan Y. Fungsi ylabel() untuk mencetak label di sumbu Y dan fungsi xlabel() untuk mencetak label sumbu X
        plt.plot([x1, x2], [y1, y2], color='red') #ini sama cuman bedanya dia deklarasiin lagi sumbu xy yang keduanya
        plt.xlim([0, 2]) # untuk menyesuaikan batas sumbu x
        plt.ylim([0, 2]) #  untuk menyesuaikan batas sumbu y
        plt.savefig(filename) #save filenya