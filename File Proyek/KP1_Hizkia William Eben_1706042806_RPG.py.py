class Bank:
    def __init__(self, nama, jenis_tabungan, saldo_awal):
        # Method untuk mendaftarkan akun BenCoin
        global keuntungan_bank
        keuntungan_bank = int(0)
        self.nama = str(nama)
        self.jenis_tabungan = str(jenis_tabungan)
        self.saldo_awal = int(saldo_awal)
        self.saldo = self.saldo_awal
        if self.jenis_tabungan in jenis_tabungan_lst:
            if self.jenis_tabungan == "Pelajar":
                self.limit = 200000
            elif self.jenis_tabungan == "Regular":
                self.limit = 250000
            elif self.jenis_tabungan == "Bisnis":
                self.limit = 500000
            elif self.jenis_tabungan == "Elit":
                self.limit = 1000000
        if self.saldo_awal > 5000:
            if self.saldo_awal <= self.limit:
                print("Nama {} telah terdaftar dengan paket {}".format(self.nama,self.jenis_tabungan))
            else:
                print("Maaf, Saldo Anda melebihi kapasitas!")
        else:
            print("Maaf, Saldo Anda kurang!")

        

    def setor(self, uang_m):
        #Method untuk Pemasukan
        global keuntungan_bank
        self.uang_m = int(uang_m)
        if self.saldo+self.uang_m <= self.limit:
            self.saldo += self.uang_m
            print("Akun telah bertambah sebesar {}".format(self.uang_m))
        elif self.saldo+self.uang_m > self.limit:
            keuntungan_bank += (self.saldo+self.uang_m)-self.limit
            self.uang_m = self.limit - self.saldo
            self.saldo = self.limit
            print("Akun telah bertambah sebesar {}".format(self.uang_m))
            

    def tarik(self, uang_t):
        #Method untuk Penarikan
        self.uang_t = int(uang_t)
        if self.uang_t>self.saldo:
            print("Transaksi gagal! Saldo tidak cukup!")
        elif self.uang_t<=self.saldo:
            self.saldo -= self.uang_t
            print("Berhasil menarik sebesar {}".format(self.uang_t))
        
        
    def transfer(self, penerima, uang_tr):
        # Method untuk transfer uang
        self.uang_tr = int(uang_tr)
        if penerima in list_nasabah:
            if self.uang_tr > self.saldo:
                print("Transaksi gagal! Saldo tidak cukup!")
            else:
                if self.uang_tr + penerima.saldo > penerima.limit:
                    penerima.saldo = penerima.limit + self.uang_tr
                    keuntungan_bank += int(penerima.saldo + self.uang_tr - penerima.limit)
                    self.uang_tr = penerima.limit - penerima.saldo
                    print("Berhasil transfer sebesar {} kepada {} ".format(self.uang_tr,penerima))
                elif self.uang_tr + penerima.saldo <= penerima.limit:
                    penerima.saldo += self.uang_tr
                    print("Berhasil transfer sebesar {} kepada {} ".format(self.uang_tr,penerima))
            

    def infoSemua():
        # Method untuk mencetak semua nama nasabah dan saldonya
        for i in list_nasabah:
            print("{} {}".format(list_nasabah[i].nama,list_nasabah[i].saldo))
        

    def infoUang():
        # Method untuk mencetak total keuntungan bank
        global keuntungan_bank
        print("BANK Mendapat Keuntungan sebesar {}".format(keuntungan_bank))

# Dictionary untuk menyimpan objek nasabah berdasarkan namanya
list_nasabah = {}

# List berisi daftar perintah yang valid
daftar_perintah = ["DAFTAR","TARIK","SETOR","TRANSFER","INFO"]

# List jenis tabungan yang valid
jenis_tabungan_lst = ["Pelajar","Regular","Bisnis","Elit"]

# Set variabel keuntungan Bank
keuntungan_bank = int(0)

# Main Program
# Implementasikan di bawah sini
while True:
    perintah = input().split()

    # Cek apakah perintah valid atau tidak
    if perintah[0] not in daftar_perintah:
        print("Perintah tidak valid")

    # Jika perintah valid
    else:

        # Menjalankan perintah Daftar
        if perintah[0] == "DAFTAR":

            # Cek apakah nama nasabah sudah ada di dictionary
            # Cek apakah jenis tabunagan valid
            if(perintah[1] in list_nasabah or perintah[2] not in jenis_tabungan_lst or int(perintah[3]) <= 0):
                print("Tidak bisa melakukan pendaftaran")

            # Jika valid, buat objek nasabah dan disimpan di dalam dictionary dengan key berupa nama Bank
            else:
                list_nasabah[perintah[1]] = Bank(perintah[1], perintah[2], int(perintah[3]))
        
        # Menjalankan perintah tarik sekaligus mengecek nama nasabah di dictionary
        elif perintah[0] == "TARIK" and perintah[1] in list_nasabah:
            list_nasabah[perintah[1]].tarik(perintah[2])

        # Menjalankan perintah setor sekaligus mengecek nama nasabah di dictionary
        elif perintah[0] == "SETOR" and perintah[1] in list_nasabah:
            list_nasabah[perintah[1]].setor(perintah[2])

        # Menjalankan perintah transfer sekaligus mengecek nama nasabah di dictionary, baik penerima maupun pengirim
        elif perintah[0] == "TRANSFER" and perintah[1] in list_nasabah and perintah[2] in list_nasabah:
            list_nasabah[perintah[1]].transfer(list_nasabah[perintah[2]],perintah[3])
        
        # Menjalankan perintah info semua
        elif perintah[0] == "INFO" and perintah[1] == "SEMUA":
            Bank.infoSemua()

        # Menjalankan perintah info keuangan
        elif perintah[0] == "INFO" and perintah[1] == "KEUANGAN":
            Bank.infoUang()
            
        #Kondisi jika nama nasabah tidak ada
        else:
            print("Nama nasabah tidak ada")


