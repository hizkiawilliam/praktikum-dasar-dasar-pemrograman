'''
import string

#meminta input
key1 = int(input("Masukkan Key 1: ").lower())
key2 = int(input("Masukkan Key 2: ").lower())
pesan = input("Masukkan Pesan : ").lower()

#set variable
hasil = ""
reverse2 = ""
count = 0

#slice input pesan sesuai key1
#membalik input pesan sesuai
for i in range(len(pesan)):
    split = pesan[count:count+key1:]
    reverse1 = split[::-1]
    count+=key1
    reverse2 = reverse2 + reverse1

#mencipher hasil reverse2 dengan Caesar Cipher
for i in range(len(reverse2)):
    #memeriksa jika input pesan adalah alphabet
    if 97 <= ord(reverse2[i]) <= 122:                   
        code = ord(reverse2[i])%97 + key2               
        hasil += chr((code%26) + 97)
        success = True
    #jika input pesan mengandung non-aplhabet
    else:
        print("Tidak bisa mengenkripsi non-alphabet")
        success = False
        break
#print hasil apabila pesan tidak mengandung non-alphabet    
if success == True:
    print("Pesan hasil enkripsi:",hasil)

'''
import string

#meminta input
key1 = int(input("Masukkan Key 1: ").lower())
key2 = int(input("Masukkan Key 2: ").lower())
pesan = input("Masukkan Pesan Rahasia : ").lower()



hasil = ""
count = 0
reverse2 = ""

for i in range(len(pesan)):
    split = pesan[count:count+key1:]
    reverse1 = split[::-1]
    count+=key1
    reverse2 = reverse2 + reverse1

for i in range(len(reverse2)):
    if 97 <= ord(reverse2[i]) <= 122:
        code = ord(reverse2[i])%97 - key2
        hasil += chr((code%26) + 97)
        success = True
    else:
        print("Tidak bisa mengdekripsi non-alphabet")
        success = False
        break

if success == True:
    print("Pesan asli:",hasil)

