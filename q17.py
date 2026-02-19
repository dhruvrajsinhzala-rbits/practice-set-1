'''Calculate the area and circumference of a circle, given its radius
'''
import math
while True:
    try:
        r=float(input("Enter radius:- "))
    except ValueError:
        print("Invalid input.")
    else:
        if r<0:
            print("Invalid input.")
            continue
        else:
            a=math.pi*r**2
            c=2*math.pi*r
            print(f"Circumference of circle is:- {c:.2f}")
            print(f"Area of circle is:- {a:.2f}")
            break