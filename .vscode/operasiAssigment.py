# Operasi yang dapat dilakukan dengan penyerdehanaan
# Operasi yang ditambahkan assigment

a = 5
print('Nilai a = ',a)
# Operasi assigment
print('=====Operasi Aritmatika=====')
a += 1 #artinya a = a + 1
print('Nilai a += 1 adalah = ',a)

a -= 1 #artinya a = a - 2
print('Nilai a -= 2 adalah = ',a)

a *= 5 #artinya a = a * 5
print('Nilai a *= 5 adalah = ',a)

a /= 5 #artinya a = a / 5
print('Nilai a /= 5 adalah = ',a)

a %= 3 #artinya a = a % 3
print('Nilai a %= 3 adalah = ',a)

a //= 5 #artinya a = a // 5
print('Nilai a //= 5 adalah = ',a)

a **= 2 #artinya a = a ** 2
print('Nilai a **= 2 adalah = ',a)

print('=====Operasi Bitwise=====')
# Operasi bitwise
# Operasi OR
print('---------------------OR')
c = True
print('Nilai dari c = ',c)
c |= False
print('Nilai c |= False adalah ',c)
c = False
print('Nilai dari c = ',c)
c |= False
print('Nilai c |= False adalah ',c)
# Operasi AND
print('---------------------AND')
c = True
print('Nilai dari c = ',c)
c &= False
print('Nilai c &= False adalah ',c)
c = False
print('Nilai dari c = ',c)
c &= False
print('Nilai c &= False adalah ',c)
# Operasi XOR
print('---------------------XOR')
c = True
print('Nilai dari c = ',c)
c ^= False
print('Nilai c ^= False adalah ',c)
c = False
print('Nilai dari c = ',c)
c ^= False
print('Nilai c ^= False adalah ',c)