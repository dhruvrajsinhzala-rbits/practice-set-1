'''Implement a program that converts a given number of minutes into hours and minutes
'''
while True:
    try:
        m = int(input("Enter minutes:- "))
    except ValueError:
        print("Invalid input.")
    else:
        if m<0:
            print("Invalid input.")
            continue
        else:
            h = m//60
            m%=60
            print(f"{h} hours and {m} minutes.")
            break