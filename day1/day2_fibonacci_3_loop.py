n = int(input("你想查斐波那契数列的项数n="))
a, b =0 ,1
for i in range(n):
    a, b = b, a+b
    print(a,end="\t")