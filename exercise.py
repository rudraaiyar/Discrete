#lab1

#if a >= 10:
#	print("big")
#elif a <3 & a>10:
#	print("medium")
#else:
#	print("small")


#lab2

import math

#lab2list = [A,B,C]

def factorial(N):
    x = 1
    for i in range (1, N+1):
        x *= i
    return x

A= input()
B= input()
C= input()


ma = factorial(A) + factorial(B) + factorial(C)
result = math.factorial(A) + math.factorial(B) + math.factorial(C)

print(str(ma))


