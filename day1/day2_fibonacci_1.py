import math as m

n = int(input("请输入您想查找的斐波那契数列的项数n=："))
for i in range(n+1):
    a = ((m.sqrt(5) + 1) / 2) ** i
    b = ((m.sqrt(5) - 1) / 2) ** i
    a_i: float | int = (1 / m.sqrt(5)) * (a - b)
    print("a_i=",int(a_i))