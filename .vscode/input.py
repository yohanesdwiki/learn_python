# mengambil data string
data_nama = input("masukan nama :")
print("Halo ",data_nama, type(data_nama))

# mengambil data int atau float menggunakan casting
umur = int(input("masukan umur :"))
print("Umur mu ",umur,type(umur))

Nilai = float(input("masukan nilai :"))
print("Nilai mu ",Nilai,type(input(Nilai)))

# jika ingin mengambil data boolean harus dengan perantara int. jika ingin simple
boolean = bool(int(input("masuka nilai boolean :")))
print("nilai ini",boolean, type(boolean))