
#### Given a date in String Format , find the month inside the date. If the month number is valid , print `YES` else `NO`

'''python
Input: "03/12/1997"
Output: "Yes"
# here month is 12, so valid

Input: "31/15/2003"
Output: "No"
# here month is 15, so

Input:"29/10/2006"
Output:"Yes"

Input:"08/16/2007"
Output:"No"
'''
input="29/10/2006"

month=int(input[3:5])
if month <= 12:
    print("Yes")
else:
    print("No")



'''
### You are given a string s that contains both letters and digits. The following are the requirements:

- Print all the characters in the order they appear (excluding digits).
- Then print the sum of all digits present in the string.

```python
#test case 1
Input: abc123
Output: abc6
# explanation : abc123 - here 123 are the numbers so 1+2+3 = 6
# and remaining letters as it is are abc, so the result is abc6


# test case 2
Input: AC30BD40
Output: ACBD7

Input:JEE08V29A
Output:19

Input:OII610803
Output:18
Input:123abc456
Output:21
'''
arr=JEE08V29A
sum=0
for i in range(len(arr)):
    sum+=int(arr[i])
print(sum)





