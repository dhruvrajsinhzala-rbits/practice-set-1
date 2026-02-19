'''Given a list of numbers, find the maximum and minimum values.
'''
l=list()
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    num=int(input("Enter a number:- "))
    l.append(num)
# max_value = max(l)
# min_value = min(l)
max_value = l[0]
min_value = l[0]
for num in l:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
print(f"Maximum value:- {max_value}")
print(f"Minimum value:- {min_value}")