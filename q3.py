'''WAP to check if number is even or odd'''
while True:
    try:
        num = int(input("Enter a number:- "))
    except ValueError:
        print("Invalid input.")
    else:      
        if num % 2 == 0:
            print(f"{num} iseven.")
        else:
            print(f"{num} is odd.")
        break