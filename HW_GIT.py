
"""
Task 1
Write a recursive function for finding
the greatest common divisor of two integers.
"""

def delitel(a, b):
    if b == 0:
        return a
    return delitel(b, a % b)

num1 = int(input("Zadej první číslo: "))
num2 = int(input("Zadej druhé číslo: "))
result = delitel(num1, num2)
print(f"Největší možný dělitel těchto dvou čísel {num1} and {num2} je {result}.")