__all__=['read1','_money']#方法和变量全部要带引号
print('sss')

_money = 100
def aa():
    print('ttt')

def read1():
    print('read1%d'%_money)

def read2():
    read1()
    print('read2')

print('eee')