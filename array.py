arr=[10,20,30]

for i in range(len(arr)):
    print(arr[i])

arr.append(40);
arr.append(50);

print(arr)

arr.remove(20)
print(arr)


if 30 in arr:
    print("30 is found in the array")
else:
    print("30 is not found in the array")