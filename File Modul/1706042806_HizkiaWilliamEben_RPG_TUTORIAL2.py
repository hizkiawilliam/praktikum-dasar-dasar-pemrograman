import math #Menggunakan library math

nama = input("Nama: ")                                      #input nama
t_kej = float(input("Tingkat kejujuran "+ nama+": "))       #input nilai kejujuran
t_kec = float(input("Tingkat kecerdasan "+ nama+": "))      #input nilai kecerdasan
t_kem = float(input("Tingkat kemapanan "+ nama+": "))       #input nilai kemapanan
t_keb = float(input("Tingkat keberuntungan "+ nama+": "))   #input nilai keberuntungan
nilai_p = (3*t_kej+3*t_kec+2.5*t_kem+1.5*t_keb)             #perhitungan nilai p
nilai_q = (1/8*math.pow((t_kej+t_kec+t_kem+t_keb),2)/2)     #perhitungan nilai q

if 1<= t_kej <=10 and 1<= t_kec <=10 and 1<= t_kem <=10 and 1<= t_keb <=10: #untuk membatasi input 1<= input <=10
    print("Nilai P "+ nama+" adalah: ",round(nilai_p,2))
    print("Nilai Q "+ nama+" adalah: ",round(nilai_q,2))
    if nilai_p >=95:
        print(nama+" terlalu sempurna untuk menjadi calon suami Loly dan Lily")
    elif 85<= nilai_p <=95:
        print(nama+" lolos standar calon suami Loly dan Lily")
    elif nilai_q >= 45:
        print(nama+" lolos standar calon suami Lily")
    else:
        print(nama+" tidak lolos standar siapapun :(")
else:
    print("Nilai tidak sesuai\nHarus diantara 1 dan 10")


    
