n=int(input("请问您想输出哪个数以内的乘法表："))
for j in range(1,n+1):
    for i in range(1,j+1):
        print(f"{i}×{j}=",i*j,end= "\t")
    print()
