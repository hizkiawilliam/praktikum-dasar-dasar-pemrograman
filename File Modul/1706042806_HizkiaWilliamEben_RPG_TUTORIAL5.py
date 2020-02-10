import math
#Membuat fungsi A
def funcA(x,y):
    return x**2+y**2
#Membuat fungsi B
def funcB(x,y):
    return math.floor(math.sqrt(int(funcA(x,y)))+(int(a)//int(b)))
#Membuat fungsi C
def funcC(x,y):
    return funcB(x,y)/2
#Membuat fungsi D
def funcD(x,y):
    return (int(funcA(x,y))+int(funcC(x,y))/x)//(int(funcA(x,y))+int(funcC(x,y))//y)


#input_file = str(input("Masukkan file : "))
input_file='text.txt'
#Try untuk mencegah error
try:
    #Membuka file input dan file output
    my_file = open(input_file,'r')
    out_file = open('out.out','w')

    #Menjadikan setiap line dalam file my_file menjadi list
    lst = my_file.read().split()
    list(lst)
    
    #Memeriksa setiap komponen dalam list lst
    #Menentukan fungsi yang akan dieksekusi
    for i in lst:
        if i == 'FUNGSI-A':
            try:
                a = lst[lst.index(i)+1]
                b = lst[lst.index(i)+2]
                result = funcA(int(a),int(b))
                print('HASIL FUNGSi-A'+'('+str(a)+','+str(b)+') =',str(result),file=out_file)
            except ZeroDivisionError:
                print('Pembagian dengan nol',file=out_file)
                continue
        if i == 'FUNGSI-B':
            try:
                a = lst[lst.index(i)+1]
                b = lst[lst.index(i)+2]
                result = funcB(int(a),int(b))
                print('HASIL FUNGSi-B'+'('+str(a)+','+str(b)+') =',str(result),file=out_file)
            except ZeroDivisionError:
                print('Pembagian dengan nol',file=out_file)
                continue
        if i == 'FUNGSI-C':
            try:
                a = lst[lst.index(i)+1]
                b = lst[lst.index(i)+2]
                result = funcC(int(a),int(b))
                print('HASIL FUNGSi-C'+'('+str(a)+','+str(b)+') =',str(result),file=out_file)
            except ZeroDivisionError:
                print('Pembagian dengan nol',file=out_file)
                continue
        if i == 'FUNGSI-D':
            try:
                a = lst[lst.index(i)+1]
                b = lst[lst.index(i)+2]
                result = funcD(int(a),int(b))
                print('HASIL FUNGSi-D'+'('+str(a)+','+str(b)+') =',str(result),file=out_file)
            except ZeroDivisionError:
                print('Pembagian dengan nol',file=out_file)
                continue
    my_file.close()
    out_file.close()
#Eksekusi jika file tidak ditemukan
except FileNotFoundError:
    print('File tidak ditemukan')
#Eksekusi jika tipe data salah
except ValueError:
    print('Terdapat kesalahan tipe data')
            
