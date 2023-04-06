import random

# Menghasilkan angka acak antara 1 dan 10
angka_acak = random.randint(1, 10)

# Memberikan kesempatan menebak kepada pemain
print("Tebak angka antara 1 dan 10!")
tebakan = int(input("Masukkan tebakanmu: "))

# Loop untuk memberikan kesempatan menebak lebih dari satu kali
while tebakan != angka_acak:
    if tebakan > angka_acak:
        print("Angka terlalu besar, coba lagi.")
    else:
        print("Angka terlalu kecil, coba lagi.")
    tebakan = int(input("Masukkan tebakanmu: "))

# Jika tebakan benar, cetak pesan kemenangan
print("Selamat! Angka yang benar adalah", angka_acak, "dan kamu berhasil menebaknya!")
