from math import sqrt

def Welcome():
    print("\nHerzlich wilkommen, mit diesem Programm wirst du in der lage sein die quadratische Gleichung(ax^2 + bx + c = 0) zu lösen")
    print("------------------------------------------------------------------------------------------------------------------------")

def UserInput():
    global a
    a = float(input("Koeffizient a: "))
    global b
    b = float(input("Koeffizient b: "))
    global c
    c = float(input("Koeffizient c: "))

def Calculation():
    if a != 0:
        D = b*b-4*a*c
        print(D)
        if D > 0:
            print("Die Gleichung hat zwei verschiedene Lösungen:")
            x1 = (-b + sqrt(D))/(2*a)
            x2 = (-b - sqrt(D))/(2*a)
            print(f"x1 = {x1}, x2 = {x2}")
        elif D == 0:
            print("Die Gleichung hat eine Lösung:")
            x1 = -b/(2.0*a)
            print(f"x1 = x2 = {x1}")
        else:
            print("Die Gleichung hat keine reele Lösung")
    else:
        if b != 0.0:
            x = -c/b
            print("Die Gleichung ist linear und hat somit eine Lösung:")
            print(f"x = {x}")
        else:
            if c != 0.0:
                print("Die Gleichung ist unlösbar")
            else:
                print("Die Gleichung hat unendlich viele Lösungen")

Welcome()
UserInput()
Calculation()