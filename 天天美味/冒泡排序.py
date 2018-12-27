arry = [1, 2, 5, 3, 6, 8, 4]
# print(len(arry))
for i in range(len(arry)-1):
    for j in range(len(arry)-1-i):
        if arry[j] > arry[j+1]:
            arry[j],arry[j+1] = arry[j+1],arry[j]
    # print(arry[i])
for i in arry:
    print(i)

