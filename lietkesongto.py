n = int(input())
if n == 1:
  print(0)
elif n == 2:
  print(1)
elif n>2:
  count = 1
  for i in range(3, n+1, 2):
    for j in range(3, i):
      if(i%j == 0):
        break
    else:
      count+=1
  else:
    print(count)