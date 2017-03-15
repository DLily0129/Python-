diet = ["西红柿","花椰菜","黄瓜","牛排","虾仁"]
for x in diet :
    for y in diet :
        if x!=y :
            print("%s、%s"%(x,y),end='  ')
    print('\n')
