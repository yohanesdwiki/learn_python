# latihan konversi suhu dengan menggunakan python
Celcius = float(input("Masukan Suhu dalam Celcius : "))
print("Suhu dalam celcius = ",Celcius)

# Celcius to Reamur
Reamur = 4/5 * Celcius
print("suhu dalam reamur adalah ",Reamur)

# Celcius to Farenheit
Farenheit = (9/5 * Celcius) + 32
print("Suhu dalam farenheit adalah ",Farenheit)

# Celcius to Kelvin
Kelvin = Celcius + 273
print("Suhu dalam kelvin adalah ",Kelvin)

print("======PR========")
# input farenheit ke kelvin
farenheit = float(input("Masukan nilai farenheit : "))
print("suhu di dalam farenheit",farenheit,"farenheit")
celcius = (farenheit-32)*9/5
Kelvin = celcius + 273
print("Suhu di dalam kelvin ",celcius,"kelvin")

print("======PR======")
# input kelvin ke farenheit
kelvin = float(input("Masukan suhu kelvin : "))
print("suhu dalam Kelvin ",kelvin," Kelvin")
celcius = kelvin-273
farenheit = 9/5*farenheit+32
print("Nilai dalam farenheit adalah ",farenheit," Farenheit")