def reverseString(s):                           #define fungsi reverseString
    if s == "":                                 #periksa jika s adalah string kosong
        return s
    else:
        return reverseString(s[1:]) + s[0]      #mengembalikan rekursif s yang hanya index selanjutnya ditambah s[0]
    
def checkDuplicate(num,lst):                    #define fungsi checkDuplicate
    if lst == []:                               #periksa jika lst kosong
        return 0
    if lst[0] == num:                           #jika input angka sama dengan angka pada list
        return 1 + checkDuplicate(num,lst[1:])  #tambah 1 sebagai counter dan cocokan kembali input angka dengan angka pada list selanjutnya
    else:
        return 0 + checkDuplicate(num,lst[1:])  #jika tidak cocok, tetap lanjut ke angka pada list selanjutnya
            
print("Mau pilih nomor berapa? [1 atau 2]")
print("1] Reverse String")
print("2] Count Existence")
choice = input()                                #input pilihan
if choice == '1':                               #jika pilihan adalah 1
    print("Masukan sebuah string")
    string = input()                            #meminta input string yang akan dibalik
    reversed_string = reverseString(string)     #assign var reversed string dengan hasil return fungsi reverseString(string)
    print("{} dibalik menjadi {}".format(string,reversed_string))
elif choice == '2':                             #jika pilihan adalah 2
    print("Masukan sebuah angka")
    angka = input()                             #meminta input angka yang akan di cek
    print("Masukkan kumpulan angka yang akan dimasukkan ke dalam list")
    lst_angka_input = input()                   #meminta input list angka
    lst_angka = lst_angka_input.split()         #membuat input menjadi list
    print("Jumlah angka {} pada list tersebut adalah {}".format(angka,checkDuplicate(angka,lst_angka)))
    
