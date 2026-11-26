x = 9
angka = 1
jumlah_tampil = 0
angka_lewati = x + 2
angka_berhenti = x + 11

print("x =", x)
print("angka_lewati =", angka_lewati)
print("angka_berhenti =", angka_berhenti)

while True:
    if angka == angka_berhenti:
        break
    if angka == angka_lewati:
        angka += 1
        continue
    print(angka)
    jumlah_tampil += 1
    angka += 1

print("Jumlah angka ditampilkan:", jumlah_tampil)
print("Program selesai.")