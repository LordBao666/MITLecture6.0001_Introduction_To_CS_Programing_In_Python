"""
@Author  : Lord_Bao
@Date    : 2021/3/4

"""
# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k / 2.0
num_guess = 0
while abs(guess * guess - k) >= epsilon:
    num_guess += 1
    print("guess ", guess)
    guess = guess - (((guess ** 2) - k) / (2 * guess))
print("numGuess = ", num_guess)
print('Square root of', k, 'is about', guess)
