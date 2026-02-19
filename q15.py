'''Concatenate a list of names into a single string separated by spaces.
'''
l=list()
n=int(input("Enter the number of elements:- "))
i=0
while i<n:
    s=input("Enter a string:- ")
    if s=="":
        print("Invalid input. Please try again.")
    else:        
        l.append(s)
        i+=1
print(f"List of strings:- {l}")
print(f"Concatenated string:- {' '.join(l)}")
