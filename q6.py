'''Calculate the compound interest for a given principal amount, 
interest rate, and time period
'''
while True:
    try:
        principal = float(input("Principal amount:- "))
        rate = float(input("Interest rate (in percentage):- "))/100
        time = float(input("Time period (in years):- "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    else:
        if principal < 0 or rate < 0 or time < 0:
            print("Principal, rate, and time must be positive.")
        else:
            break
amount = principal * (1 + rate) ** time
print(f"The compound interest is:- {amount - principal}")