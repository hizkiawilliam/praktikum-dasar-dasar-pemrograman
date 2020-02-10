# Tidak wajib menggunakan template ini
# Template ini boleh dimodifikasi

class servant:
    def __init__(self, nama, tipe, power):
        # Todo buatlah konstruktor untuk membuat objek Servant
        self.nama = nama
        self.tipe = tipe
        self.power = power
        self.healthy = True
        self.level = 1

    def train(self):
        # Implementasikan method Train
        self.power += (0.1*self.power)
        print(str(self.nama)+" berlatih keras dan kekuatannya meningkat menjadi "+str(self.power))
        
    
    def battle(self, enemy):
        # Implementasikan method Battle
        if self.power>enemy.power:
            selisih = self.power - enemy.power
            print(str(self.nama)+" menang dalam pertarungan dan "+str(enemy.name)+" menjadi terluka. Selisih kekuatan mereka adalah "+str(selisih))
            self.level += 1
        elif self.power<enemy.power:
            print(str(enemy.nama)+" menang dalam pertarungan dan "+str(self.name)+" menjadi terluka. Selisih kekuatan mereka adalah "+str(selisih))
            enemy.level +=1
        else:
            print(str(self.nama)+" dan "+str(enemy.name)+" dalam pertarungan sengit yang berakhir seri. Keduanya menjadi terluka")
        
        
    def serangan(self):
        # Method serangan untuk menghitung kekuatan serangan
        print("Kekuatan serangan : "+str(self.power))

    def heal(self):
        # Method untuk menyembuhkan diri
        if self.healthy == False:
            self.healthy = True
            print("Servant "+str(self.nama)+" berhasil dipulihkan dan kembali sehat")
        elif self.healthy == True:
            print("Servant "+str(self.nama)+" keadaannya masih sehat")

    def stats(self):
        # Implementasikan method stats
        print("Nama : "+str(self.nama))
        print("Tipe : "+str(self.tipe))
        print("Power : "+str(self.power))
        print("Level : "+str(self.level))
        if self.healthy == True:
            print("Status : Sehat")
        elif self.healthy == False:
            print("Status : Terluka")

# Dictionary untuk menyimpan objek Servant
daftar_servant = {}

# List daftar tipe Servant
tipe_servant = ["Saber","Lancer","Archer","Caster","Assassin","Rider","Berserker"]

# List daftar perintah yang valid
daftar_perintah = ["SUMMON","TRAIN","BATTLE","HEAL","STATS"]

while True:
    # Implementasikan Main Program disini
    perintah = input().split()
    set(perintah)
    
    if perintah[0] == daftar_perintah[0]:
            if int(perintah[3])>=0:
                print("Berhasil memanggil Servant dengan nama "+str(perintah[1])+" dengan tipe "+str(perintah[2]))
                daftar_servant[perintah[1]] = servant(str(perintah[1]),perintah[2],int(str(perintah[3])))
            else:
                print("Tidak bisa memanggil Servant karena kesalahan")

    elif perintah[0] == daftar_perintah[1]:
            daftar_servant[perintah[1]].train()

    elif perintah[0] == daftar_perintah[2]:
            daftar_servant[perintah[1]].battle(perintah[2])

    elif perintah[0] == daftar_perintah[3]:
            daftar_servant[perintah[1]].heal()

    elif perintah[0] == daftar_perintah[4]:
            daftar_servant[perintah[1]].stats()

    else:
            print("Perintah tidak valid")
 
    
