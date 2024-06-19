size=int(input("nhap so hàng: "))
for i in range(size, 0, -1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("")