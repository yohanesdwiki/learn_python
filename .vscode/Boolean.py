# Operasi logika boolean 
# not, and, or, xor

# Operasi Not
print("====NOT====")
a = True
c = not a
print("nilai a adalah ",a)
print('-------------NOT')
print("Nilai c adalah ",c)
# Operasi OR (Minimal terdapat 1 nilai True)
print("====OR====")
a = True
b = False
c = a or b
print('a or b ',' =',c)
a = False
b = False
c = a or b
print('a or b ',' =',c)
a = True
b = True
c = a or b
print('a or b ',' =',c)
a = False
b = True
c = a or b
print('a or b ',' =',c)
# Operasi AND (Harus semua True)
print("====AND====")
a = True
b = False
c = a and b
print('a or b ',' =',c)
a = False
b = False
c = a and b
print('a or b ',' =',c)
a = True
b = True
c = a and b
print('a or b ',' =',c)
a = False
b = True
c = a and b
print('a or b ',' =',c)
# Operasi OR (Minimal terdapat 1 nilai True)
print("====OR====")
a = True
b = False
c = a or b
print('a or b ',' =',c)
a = False
b = False
c = a or b
print('a or b ',' =',c)
a = True
b = True
c = a or b
print('a or b ',' =',c)
a = False
b = True
c = a or b
print('a or b ',' =',c)
# Operasi XOR (Akan bernilai true, jika kesalah satu bernilai true dan sisanya false)
print("====XOR====")
a = True
b = False
c = a ^ b
print('a xor b ',' =',c)
a = False
b = False
c = a ^ b
print('a xor b ',' =',c)
a = True
b = True
c = a ^ b
print('a xor b ',' =',c)
a = False
b = True
c = a ^ b
print('a xor b ',' =',c)