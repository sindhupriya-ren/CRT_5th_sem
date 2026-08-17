'''
input : [12,45,63,20,96,25,10]
output : [12,20,96,10]
'''
arr = list(map(int,input().split()))
i = 0 
for j in range(len(arr)):
    if arr[j] % 2 == 0:
        arr[i] = arr[j]
        i += 1 
print(arr[:i])
    

