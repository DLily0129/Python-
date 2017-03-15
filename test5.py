num = int(input("请输入一个正整数N:"))
sum = 0
for i in range (1,num+1) :
    sum = sum + i
print ("1到N求和结果为:%d"%sum)

#打印九九乘法表
for i in range(1,10) :
    for j in range(i,10) :
        print ("%d*%d=%d"%(i,j,i*j),end=' ')
    print ('\n')

#计算1!+2!+...+n!
num = int(input("请输入一个正整数n（n<=10）:"))
p = 1
sum = 0
for i in range(1,num+1) :
    p = p*i
    sum = sum + p
print ("运行结果为:%d"%sum)
