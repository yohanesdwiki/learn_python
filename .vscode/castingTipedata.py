# Casting adalah merubah tipe data

# tipe data asli INTEGER
print("====INTEGER====")
data_int = 10
print("data : ",data_int,", bertipe = ", type(data_int))

# mengCasting tipe data
data_str = str(data_int)
print("data : ",data_str,", bertipe = ", type(data_str))

data_float = float(data_int)
print("data : ",data_float,", bertipe = ", type(data_float))

data_bool = bool(data_int)
print("data : ",data_bool,", bertipe = ", type(data_bool))

# tipe data asli FLOAT
print("====FLOAT====")
data_float = 10.5
print("data : ",data_float,", bertipe = ", type(data_float))

# mengCasting tipe data
data_str = str(data_float)
print("data : ",data_str,", bertipe = ", type(data_str))

data_int = int(data_float)
print("data : ",data_int,", bertipe = ", type(data_int))

data_bool = bool(data_float)
print("data : ",data_bool,", bertipe = ", type(data_bool))