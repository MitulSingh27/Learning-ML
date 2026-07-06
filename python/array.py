'''
🧠 What is an Array?

Think of an array like a row of lockers:

[ 10 | 20 | 30 | 40 | 50 ]
   0    1    2    3    4   ← index

Each value is stored in a position called an index

Indexing starts from 0 (very important)

👉 In Python, arrays are usually implemented using lists

arr = [10, 20, 30, 40, 50]
🔑 Basic Operations (You MUST know these)
1. Accessing Elements
arr = [10, 20, 30, 40]

print(arr[0])  # 10
print(arr[2])  # 30

👉 Time Complexity: O(1) (very fast ⚡)

2. Updating Elements
arr[1] = 99
print(arr)  # [10, 99, 30, 40]
3. Adding Elements
➤ At the end (fast)
arr.append(60)

👉 O(1)

➤ At a specific position (slower)
arr.insert(1, 15)

👉 O(n) (because elements shift)

4. Deleting Elements
arr.pop()        # removes last
arr.pop(1)       # removes index 1
arr.remove(30)   # removes value 30

👉 Usually O(n)

🔁 Traversing an Array
Method 1 (best)
for x in arr:
    print(x)
Method 2 (with index)
for i in range(len(arr)):
    print(arr[i])
🔍 Searching in Array
1. Linear Search (basic)
arr = [10, 20, 30, 40]

target = 30

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)

👉 Time Complexity: O(n)

2. Binary Search (VERY IMPORTANT 🔥)

👉 Works only on sorted arrays

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
📊 Important Concepts
🧩 1. Static vs Dynamic Arrays

Python lists = dynamic arrays

They resize automatically

🧩 2. Time Complexity Summary
Operation	Time
Access	O(1)
Append	O(1)
Insert/Delete	O(n)
Search	O(n)
🧠 Common Patterns (VERY IMPORTANT FOR INTERVIEWS)
1. Two Pointer Technique
arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    print(arr[left], arr[right])
    left += 1
    right -= 1
2. Sliding Window (super powerful 🔥)

Example: max sum of subarray of size k

arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)

print(max_sum)

'''