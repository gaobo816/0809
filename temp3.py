# import re
#
# print(re)
#
# l = [5,6,7,8,9]
#
# print(l[3:5])

def func1(t,*args,**kwgrgs):
    print(args)
    print(kwgrgs)


print(func1(5,3,2,1,p=0,o=999))
