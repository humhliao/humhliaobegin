size = 8
for i in range(1,size+1):
    for j in range(1, i+1):
        print(i, end=" ")
    for j in range(i+1,size+1):
        print(j, end=" ")
    print()
