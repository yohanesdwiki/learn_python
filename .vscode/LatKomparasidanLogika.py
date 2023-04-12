# menggabungkan kedua logic komparasi dengan boolean

# +++++3-------10+++++

inputUser = float(input("masukan nlai kurang dari 3 \natau lebih dari 10 : "))
# ++++++++++3----
isKurangDari = inputUser < 3
print("Nilai kurang dari 3 :", isKurangDari)
# ---------10++++
isLebihDari = inputUser > 10
print("Nilai kurang dari 10 :", isLebihDari)
# hasil
hasil = isKurangDari or isLebihDari
print("Nilai yang kamu masukan adalah =", hasil)

# kasus irisan
# ----3++++++++++10----
inputUser = float(input("Masukan Nilai yang lebih \ndari 3 dan kurang dari 10 : "))
# ----3++++++++++
isLebihDari = inputUser >= 3
print("Nilai lebih dari 3 = ",inputUser)
# ++++++++++++10----
isKurangDari = inputUser <= 10
print("Nilai kurang dari 10 = ",inputUser)
# hasil
hasil = isKurangDari and isLebihDari
print("Nilai yang kamu masukan =", hasil)