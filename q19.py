'''Create a function to count the number of vowels in a given string
'''
def vowel(s):
    count = 0
    for i in s:
        if i in 'aeiou':
            count += 1
    return count
s=input('Enter a string:- ').lower()
print(f"Total number of vowels:- {vowel(s)}")