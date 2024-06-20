size = int(input())

# In tam giác sao hướng lên
for i in range(1, size + 2):
    # In khoảng trắng
    for j in range(size + 1- i):
        print(" ", end="")
    # In dấu sao
    for j in range(i):
        print("* ", end="")
    print("")

# In tam giác sao hướng xuống
for i in range(size , 0, -1):
    # In khoảng trắng
    for j in range(size+1 - i):
        print(" ", end="")
    # In dấu sao
    for j in range(i):
        print("* ", end="")
    print("")
