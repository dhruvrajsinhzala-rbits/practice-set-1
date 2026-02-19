'''Calculate the sum of digits of a given number.
'''
n=int(input("Enter a number:- "))
sum=0
temp=n
while temp>0:
    sum+=temp%10
    temp//=10
print(f"The sum of digits of {n} is {sum}.")