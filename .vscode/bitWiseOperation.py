# Operator bitwise adalah operasi berbandingan binary

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('-------------------------------------')
print('nilai :',c,',binary :',format(c,'08b'))

# bitwise AND (&)
c = a & b
print('========AND========')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('-------------------------------------')
print('nilai :',c,',binary :',format(c,'08b'))

# bitwise XOR (^)
c = a ^ b
print('========XOR========')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('-------------------------------------')
print('nilai :',c,',binary :',format(c,'08b'))

# Shift right (>>)
c = a >> 2
print('========>>========')
print('nilai :',a,',binary :',format(a,'08b'))
print('-------------------------------------')
print('nilai :',c,',binary :',format(c,'08b'))

# Shift left (<<)
c = a << 2
print('========>>========')
print('nilai :',a,',binary :',format(a,'08b'))
print('-------------------------------------')
print('nilai :',c,',binary :',format(c,'08b'))