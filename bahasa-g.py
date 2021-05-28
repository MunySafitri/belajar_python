kata = input("Input Kalimat: ")

print("Output bahasa g: " , end="")

for i in kata:
    print(i, end="")
    if i =="a":
        print("ga", end="")
    elif i== "i":
        print("gi", end="")
    elif i =="u":
        print("gu", end="")
    elif i =="e":
        print("ge", end="")
    elif i =="o":
        print("go", end="")
print("")
