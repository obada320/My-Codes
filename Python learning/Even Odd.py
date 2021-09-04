#Even odd Project
# taking inputs and turning it to intger
limit , index = input().split() # 10 , 3
limit = int(limit)
index = int(index)
# even and odd list
even = []
odd = []


for i in range(1,limit + 1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

list = odd + even
print(list[-1])