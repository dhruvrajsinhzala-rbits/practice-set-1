'''Given a list of integers, find all the even numbers and store them in a new list)
'''
l=eval(input("Enter a list:- "))
even=[x for x in l if x%2==0]
print(f"Even number list:- {even}")