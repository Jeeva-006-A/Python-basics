# Input: [12,5,8,19,22,3]
#  Output: 12 8 22

# num=[12,5,8,19,22,3]
# for i in range(len(num)):
#     if i % 2 == 0:
#         print(num[i],end=" ")

# Sum of all positive numbers
#  Input: [-2,10,-5,7,-1]
#  Output: 17

# num=[-2,10,-5,7,-1]
# sum=0
# for i in range(len(num)):
#     if num[i] > 0:
#         sum+=num[i]
# print(sum)

# Sum of all negative numbers
#  Input: [-2,10,-5,7,-1]
#  Output: -8

# num=[-2,10,-5,7,-1]
# sum=0
# for i in range(len(num)):
#     if num[i] < 0:
#         sum+=num[i]
# print(sum)

# Input: [0,5,0,3,0]
#  Output: 3

# num=[0,5,0,3,0]
# count=0
# for i in range(len(num)):
#     if num[i] == 0:
#         count+=1
# print(count)

# Create new list of numbers > 50
#  Input: [10,55,49,60,50]
#  Output: [55,60]

# num =[10,55,49,60,50]
# new_list=[]
# for i in range(len(num)):
#     if num[i] > 50:
#         new_list.append(num[i])
# print(new_list)

# Count numbers divisible by 3
#  Input: [3,6,7,9,10]
#  Output: 3

num = [3,6,7,9,10]
count=0
for i in range