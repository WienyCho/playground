import math as m

n = int(input("请输入您想查找的斐波那契数列的项数n=："))
for i in range(n):
    a = ((1+m.sqrt(5)) / 2) ** (i+1)
    b = ((1-m.sqrt(5)) / 2) ** (i+1)
    a_i = (1 / m.sqrt(5)) * (a - b)
    print(int(a_i), end = "\t")