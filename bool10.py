def check_perfect_square(a):
    if a >= 0:
        sqrt_a = int(a ** 0.5)
        return sqrt_a * sqrt_a == a
    else:
        return False
print(check_perfect_square(16))   # True
print(check_perfect_square(25))   # True
print(check_perfect_square(10))   # False
print(check_perfect_square(-4))   # False
