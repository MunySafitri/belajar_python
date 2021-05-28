print("Selamat Datang di game Kuis")
print("berapa hasil 1+1")
print("a.1   b.2   c.3   d.4")
i=input("masukkan jawaban anda:")
count=0
if(i=="b"):
    print(" benar!")
    count=count+1
else:
    print(" Salah!")
    
print("berapa hasil 2+2")
print("a.7   b.6   c.5   d.4")
r=input("masukkan jawaban anda:")
if(r=="d"):
    print(" benar!")
    count=count+1
else:
    print(" Salah!")
print("berapa hasil 7+2")
print("a.5   b.10   c.9   d.4")
l=input("masukkan jawaban anda:")
if(l=="c"):
    print(" benar!")
    count=count+1
else:
    print(" Salah!")
    
print("skor yang anda dapatkan adalah: ",count)
