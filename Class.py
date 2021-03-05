class student():
    
    def nama(self):
        print("Nama   :", self.full_name)
        
    def get_age (self):
        print("Usia   :", self.age)
    def get_alamat (self):
        print("Alamat :", self.alamat)
    def get_status (self):
        print("Status :", self.status)
budi = student()

budi.full_name = "Budi Permana"
budi.age = "21"
budi.alamat = "Bandung"
budi.status = "Mahasiswa"

budi.nama()
budi.get_age()
budi.get_alamat()
budi.get_status()
