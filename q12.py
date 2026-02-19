'''Create a program that takes a temperature in Celsius and converts it to Kelvin.
'''
while True:
    try:
        c=float(input("Enter the temprature in celsius:- "))
    except ValueError:
        print("Invalid input.")
    else:
        k=c+273.15
        print(f"Temprature in kelvin:- {k:.2f}")
        break