# arr=[1,7,16,17,18,25,29,33,45,]
# arr.append(69)
# print(arr)
# arr.insert(4,77)
# print(arr)
# arr.extend([25,35,65,75])
# print(arr)
# arr.pop()
# print(arr)

# arr=[1,7,16,17,18,25,29,33,45]
# for i in range(len(arr)):
#     if arr[i] > 15:
#      print(arr[i])

# for a in arr:
#     print(arr)

# names=['Jeeva','Nathiya','Yashika','Kamalesh','Anto','Nagaraj']
# marks=[80,94,96,97,85,75]
# pass_mark=70

# for i in range(len(names)):
#     print(names[i])

# for  name in names:
#     print(name)

# for i in range(len(names)):
#     if marks[i] > pass_mark:
#         print(names[i])


num_list=[20,11,-7,-33,45,-16,-29,25,-3]
count=0

for i in range(len(num_list)):
    if num_list[i] < 0:
        count=count+1
print(count)