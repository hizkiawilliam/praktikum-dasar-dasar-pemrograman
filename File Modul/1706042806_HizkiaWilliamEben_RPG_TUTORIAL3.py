#masukkan input
kode = input("Masukkan kode mentah : ")
namlok = input("Masukkan nama lokasi : ")
biner = input("Masukkan biner : ")

#memeriksa input
if 1<=len(kode)<=5:
    password = ("Anja5")
elif 6<=len(kode)<=10:
    if namlok == 'bukit':
        password = str("y3KAI1")
    elif namlok == 'matahari':
        password = str("AkUK4mu")
    else:
        password = str("c4p3DEh")
elif 11<=len(kode)<=15:
    if namlok == 'mikrofon':
        password = str("g46Un4")
    else:
        password = str("54nsAE")
elif 16<=len(kode)<=20:
    if namlok == 'taman':
        password = str("k3PO")
    else:
        password = str("s3LOW")
elif 21<=len(kode)<=100:
    if namlok == 'dapur':
        password = str("s04L1niEZ")
    else:
        password = str("C4b5KUy")
else:
        password = str("x00000x")

#konversi biner
n=len(biner)
konversi=0
for i in range(1,n+1):
      konversi=konversi+ int(biner[i-1])*2**(n-i)
      
#hasil cetak
print("")
print("========Dipsi LIVE Hack========")
print("==========SANDI DATA===========")
print("Kode awal sandi : "+password)
print("Kode awal sandi : "+str(konversi))
print("Hasil konversi akhir : "+ "///"+password+"///"+str(konversi)+"///")
print("===============================")
print("Sandi berhasil diterjemahkan!\nPencuri akan segera ditangkap!")

