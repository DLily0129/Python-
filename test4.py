num=int(input("请输入一个数:"))
if num == 1 :
    print("该数不是素数")
else :
    for i in range(2,num) :
        if num % i == 0 :
            print("该数不是素数")
            break
    else :     #当循环被 break 结束时, else 不执行;当循环正常结束时,即没有被break, else 被执行
        print("该数是素数")
print("////////////////////////")


