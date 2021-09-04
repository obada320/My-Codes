def add(*num : float):
    return num + num

print(add(1,1))

List = [3,5,4,7,3,8,9,5]

def sortout(list : list,outdata):
    L = len(list)
    for i in range(1,L):
        key = list[i]
        j = i - 1
        while j >= 0:
            if key < list[j]:
                list[j+1] = list[j]
                list[j] = key
            j = j - 1
    total1 = outdata
    total2 = list
    total = total1 = total2
    return outdata

a = 1
b = List

print(sortout(b,a))
