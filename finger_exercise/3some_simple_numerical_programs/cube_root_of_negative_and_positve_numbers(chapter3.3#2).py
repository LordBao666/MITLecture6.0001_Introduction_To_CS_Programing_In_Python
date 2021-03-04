"""
@Author  : Lord_Bao
@Date    : 2021/3/4

"""


x = float(input("input a number: "))
epsilon = 0.01
numGuesses = 0

low = -1
high = -1
# 如果x是正数
if x > 0:
    low = 0.0
    high = max(1.0, x)
else:
    high = 0.0
    low = min(-1.0, x)

ans = (high + low) / 2.0
while abs(ans ** 3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans ** 3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print("numGuess = ", numGuesses)
print(ans, 'is close to cube root of', x)
