import math as m

i = int(input("请输入您想查找的斐波那契数列的项数n=："))
a = ((m.sqrt(5) + 1) / 2) ** i
b = ((m.sqrt(5) - 1) / 2) ** i
a_i = (1 / m.sqrt(5)) * (a - b)
print(int(a_i))