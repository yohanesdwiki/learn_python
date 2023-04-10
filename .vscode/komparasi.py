# komparasi adalah sebuah operasi perbandingan untuk membandingkan sejumlah nilai
# >,<,>=,<=,==,!=,is,is not

a = 3
b = 4
# operasi lebih besar dari (>)
print("====Lebih Besar====")
hasil = a > b
print("hasil dari ",a," >",b," =",hasil)
hasil = a > 2
print("hasil dari ",a," >",2," =",hasil)
hasil = a > a
print("hasil dari ",b," >",b," =",hasil)
# operasi Kurang dari (<)
print("====Kurang Dari====")
hasil = a < b
print("hasil dari ",a," <",b," =",hasil)
hasil = a < 2
print("hasil dari ",a," <",2," =",hasil)
hasil = b < b
print("hasil dari ",b," <",b," =",hasil)
# kurang dari sama dengan (<=)
print("====Kurang Dari Sama Dengan====")
hasil = a >= b
print("hasil dari ",a," >=",b," =",hasil)
hasil = a >= 2
print("hasil dari ",a," >=",2," =",hasil)
hasil = b >= a
print("hasil dari ",b," >=",b," =",hasil)
# lebih dari sama dengan (>=)
print("====Lebih dari sama dengan====")
hasil = a >= b
print("hasil dari ",a," >=",b," =",hasil)
hasil = a >= 2
print("hasil dari ",a," >=",2," =",hasil)
hasil = b >= a
print("hasil dari ",b," >=",b," =",hasil)
# Operasi sama dengan (==)
print("===Sama Dengan====")
hasil = a == b
print("hasil dari ",a," ==",b," =",hasil)
hasil = a == 2
print("hasil dari ",a," ==",2," =",hasil)
hasil = b == b
print("hasil dari ",b," ==",b," =",hasil)
# Operasi tidak sama dengan (!=)
print("====Tidak sama dengan====")
hasil = a != b
print("hasil dari ",a," !=",b," =",hasil)
hasil = a != 2
print("hasil dari ",a," !=",2," =",hasil)
hasil = a != a
print("hasil dari ",b," !=",b," =",hasil)
# Operasi is (is)
print("====Is====")
hasil = a is b
print("hasil dari ",a," is",b," =",hasil)
hasil = a is 2
print("hasil dari ",a," is",2," =",hasil)
hasil = a is a
print("hasil dari a"," is"," a"," =",hex(id(a)))