import math

# Get input from the user
a = float(input("Enter a (nonzero): "))
while a == 0:
    a = float(input("'a' cannot be zero.\nEnter a (nonzero): "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Calculate the discriminant
discriminant = b ** 2 - 4 * a * c
# Check the cases and calculate roots
if abs(discriminant) < 1e-9:  # Check if discriminant is close to 0
    root = -b / (2 * a)
    print(f"The equation has one root: {root}")
elif discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The equation has two roots: {root1} and {root2}")
else:
    print("The equation has no real roots")