'''Given a list of words, count the number of words with more than five characters)
'''
l=eval(input("Enter a list of words:- "))
for i in l:
    if len(i)>5:
        print(i)