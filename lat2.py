#DEKLARASI VARIABEL
a = 27 #Ini integer
b = 3.2 #Ini float
c = "Informatika" #Ini string

# MENAMPILKAN OUTPUT VARIABEL
print("Nilai dari a adalah", a , ",b adalah", b ,",dan c adalah", c) # cara 1
print("Tanggal lahir saya adalah tanggal %d"% (a)) #cara 2

# MENAMPILKAN HASIL INPUT
nama = input("Masukkan nama anda:")
umur = input("Masukkan umur anda:")
jurusan = input("Masukkan jurusan anda:")
fakultas = input("Masukkan fakultas anda:")
print("Nama saya adalah", nama, ". Dan umur saya adalah", umur,".")
print("Saya kuliah di jurusan", jurusan,"Fakultas",fakultas)

# OPERATOR
jumlah = 3 + 2
kurang = 3 - 2
pangkat = 3 ** 2
mod = 3 % 2
print("Hasil penjumlahan", jumlah)
print("Hasil pengurangan", kurang)
print("Hasil pangkat", pangkat)
print("Hasil pangkat", mod)

angka1 = input("Masukkan angka pertama: ")
angka2 = input("Masukkan angka kedua: ")
bagi = float(angka1) / float(angka2) #Konversi tipe data
print(bagi)

# MENGHAPUS VARIABEL
a = 27
print(a)

del(a) # Variabel telah dihapus
print(a)

# PERCABANGAN
nilai = input("Masukkan nilai: ")
nilai = int(nilai)

if nilai < 100 and nilai > 75:
    print("Kamu tidak perlu remedial")
elif nilai <= 75 and nilai >= 0:
    print("Kamu harus remedial")
else:
    print("Nilai kamu tidak terdefinisi")


# PERULANGAN

#while loop
i = 0

while(i <= 10):
    i += 1

    if i == 5:
        continue

    print(i)

# for loop
# paramater pertama: Batas bawah (opsional), nilai default 0
# paramater kedua: Batas atas
# paramater ketiga: Kelipatan (opsional), default kelipatan 1
for a in range(50, 101, 3):
    print("Ini pengulangan ke-",a)