x = 9
z = 19
total_sewa = 0
jumlah_transaksi = 0
persen_diskon = 5 + x
batas_diskon = 300000 + z * 1000

print("=== MINI SISTEM PENYEWAAN KENDARAAN ===")
print("x =", x, "| z =", z)
print("Diskon:", persen_diskon, "persen")
print("Batas diskon: Rp", batas_diskon)
print("1. Sepeda       - Rp 20.000/hari")
print("2. Motor Matic  - Rp 75.000/hari")
print("3. Motor Sport  - Rp 100.000/hari")
print("4. Mobil        - Rp 300.000/hari")
print("0. Selesai")

while True:
    pilihan = int(input("Pilih kendaraan (0-4): "))

    if pilihan == 0:
        break
    elif pilihan == 1:
        harga = 20000
    elif pilihan == 2:
        harga = 75000
    elif pilihan == 3:
        harga = 100000
    elif pilihan == 4:
        harga = 300000
    else:
        print("Pilihan tidak valid!")
        continue

    lama_sewa = int(input("Lama sewa (hari): "))
    if lama_sewa < 1:
        print("Lama sewa minimal 1 hari!")
        continue

    subtotal = harga * lama_sewa
    total_sewa += subtotal
    jumlah_transaksi += 1
    print("Subtotal: Rp", subtotal)

if total_sewa >= batas_diskon:
    diskon = total_sewa * persen_diskon // 100
else:
    diskon = 0

total_bayar = total_sewa - diskon

print("=== RINGKASAN ===")
print("Jumlah transaksi:", jumlah_transaksi)
print("Total sebelum diskon: Rp", total_sewa)
print("Diskon: Rp", diskon)
print("Total bayar: Rp", total_bayar)
print("Terima kasih, program selesai.")