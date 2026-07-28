a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = (b**2) - (4*a*c)

if d > 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("Roots are real and different")
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    if d == 0:
        root = -b / (2*a)
        print("Roots are real and same")
        print("Root:", root)
    else:
        real = -b / (2*a)
        imag = (-d)**0.5 / (2*a)
        print("Roots are complex and different")    

