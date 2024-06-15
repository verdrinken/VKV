from math import sqrt

A = int(input("A? "))
B = int(input("B? "))
C = int(input("C? "))

D = B ** 2 - 4 * A * C  # Calculate D

print("D =", D)

if D < 0:
    print("Geen Oplossing")
else:
    SD = sqrt(D)  # Square root of D for easier calculations in future lines
    
    if D == 0:
        print("Een oplossing")
        X = round((-B - SD) / (2 * A), 2)
        print("X =", X)
    else:
        print("Twee Oplossingen")
        X1 = round((-B - SD) / (2 * A), 2)
        X2 = round((-B + SD) / (2 * A), 2)
        print(f"X1 = {X1}\nX2 = {X2}")
