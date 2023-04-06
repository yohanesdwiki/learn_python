# tipe data: angka satuan (integer)
data_integer = 1
print("data : ", data_integer,", bertipe = ", type(data_integer))

#tipe data: angka koma (float)
data_float = 1.5
print("data : ",data_float,", bertipe = ", type(data_float))

# tipe data: Kumpulan Karakter (String)
data_str = "Yohan"
print("data : ",data_str,", bertipe = ", type(data_str))

# tipe data: Nilai benar/salah (Boolean)
data_bool = True
print("data : ",data_bool,", bertipe = ", type(data_bool))

# tipe data: bilangan kompleks
data_complex = complex(5,6)
print("data : ",data_complex,", bertipe = ", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(12.3)
print("data : ",data_c_double,", bertipe = ", type(data_c_double))