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

    # Move all zeros to end

    # Example:

    # Input:  [0,1,0,3,12]Output: [1,3,12,0,0]

arr = [0, 1, 0, 3, 12,0]

result = [x for x in arr if x != 0] + [0] * arr.count(0)

print(result)

arr = [0, 1, 0, 3, 12]

pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1

print(arr)