i=int(input("masukkan angka untuk batas bawah: "))
k=int(input("masukkan angka untuk batas atas: "))
for j in range(i,k):
    if j==1:
        continue
    if j==2:
        print(j)
    if j==3:
        print(j)
    elif j==5:
        print(j)
    elif j==7:
        print(j)
    elif (((j%2 !=0 and j%3 !=0)and j%5!=0)and j%7!=0):
        print(j)
 
