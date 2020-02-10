# DAERAH TERLARANG UNTUK DIMODIFIKASI

import os
import sys
relative_path = 'data/'

# Bagian bawah ini sama seperti membaca file dengan open(file,r) tapi ini khusus untuk relative path
# Akan dijelaskan di bab berikutnya
# Untuk sekarang tidak perlu dipikirkan karena bagian ini tidak perlu dimodifikasi

try:
    masukan = open(os.path.join(os.path.dirname(__file__),relative_path,\
              'input.in'),'r')
    price_data =   open(os.path.join(os.path.dirname(__file__),relative_path,\
              'pricelist.in'),'r')
except FileNotFoundError:
    print("File tidak ditemukan ! Hayo Jangan Modifikasi Ya")
# -------------------------------------------------------------------------------------- #
# DAERAH DI BAWAH INI BUKAN DAERAH TERLARANG



# Keyword "pass" mengartikan fungsi tersebut dilewat/diabaikan untuk dibaca
# Untuk melengkapi program, hapus kata "pass" dan lengkapi dengan rancangan kode dari Anda

sold_items = {} # Membuat dictionary baru yang akan diisi oleh KEY nya adalah JENIS PRODUK, dan VALUE nya adalah LIST/SET dari para pembeli produk itu


def printCashier(): # Silakan langkapi jika ingin mengerjakan bonus, jika TIDAK, biarkan tetap begini
    price_list = {} # Dictionary untuk menampung KEY nya JENIS PRODUK, dan VALUE nya adalah HARGA perbuah
    money_total = 0 # Total uang yang didapatkan
    pass

    # TODO BONUS:
    # Lengkapi program bagian ini, caranya terserah kepada Anda

    

def main(): # Hanya udah bagian dalam ini saja jika tidak mengerjakan bonus
    barang = {}
    for line in masukan: # Variabel "masukan" dibaca dari Build.py
        input_splitted = line.split()
        if input_splitted[0] == "TAMBAH":
                input_splitted.remove("TAMBAH")
                barang[input_splitted[0]]=set(input_splitted[1:len(input_splitted[0])])
                print(str(input_splitted[0]+" berhasil ditambahkan!"))
                 
            # TODO:
            # Lengkapi dengan membuat sebuah set untuk menampung nama pembeli di atas
            # masukkan ke dictionary yang di awal telah dibuat
        
        # TODO:
        # Manfaatkan method yang dimiliki oleh set (baca materi) untuk melengkapirangkaian operasi di bawah
        
        elif input_splitted[0] == "GABUNG":
            input_splitted.remove("GABUNG")
            print(barang[input_splitted[0]]|barang[input_splitted[1]])
            
            
        elif input_splitted[0] == "PEMBELI":
            input_splitted.remove("PEMBELI")
            print(barang[input_splitted[0]]&barang[input_splitted[1]])

        elif input_splitted[0] == "HANYA":
            input_splitted.remove("HANYA")
            print(barang[input_splitted[0]]-barang[input_splitted[1]])

        elif input_splitted[0] == "CETAK":
            if input_splitted[1] == "SEMUA":
                for keys in barang:

                   print(str(keys)+" : "+str(barang[keys]))
                
            else:
                print(str(input_splitted[1])+" : ",barang[input_splitted[1]])
          

        elif input_splitted[0] == "KELUAR":
            break
        
        else:
            print("Perintah Salah!")
main()
