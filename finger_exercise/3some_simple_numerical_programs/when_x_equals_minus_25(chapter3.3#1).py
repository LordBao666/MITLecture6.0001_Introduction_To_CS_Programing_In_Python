"""
@Author  : Lord_Bao
@Date    : 2021/3/4

"""

"""
x是负数的话，是不会存在平凡根的。low  到  high这段间隔永远不会存在合适的答案，只会死循环，其结果是
由于 ans ** why_mid_plus_1(chap10.3) 始终大于 x,那么根据算法的思路，ans被估计得较大，那么ans下一步将会更加靠近0.0，如此往复下去。
"""
x = -25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans ** 2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print("numGuess = ", numGuesses)
print(ans, 'is close to square root of', x)
