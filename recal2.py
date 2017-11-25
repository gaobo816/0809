mystr  ='1+(2*3) - 2 * ( (60-30 +((-40/5)) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

ret_mystr =mystr.replace(' ','')
import re
# my_re = '\(-?\d+[*|/]\d+\)'
ret_list =  re.findall('\(-?\d+[*|/]\d+\)',ret_mystr)
print('ret_list',ret_list)
cal_ret = []
for i in ret_list:

    t=i.strip("(").strip(')')
    print(t)
    ret = re.split("([*|/])",t)
    print(ret)
    if("*"==ret[1]):
        cal_ret.append(int(ret[0])*int(ret[2]))
    elif("/"==ret[1]):
        cal_ret.append(int(ret[0])*int(ret[2]))
    else:
        print("获取的字符串有误")
        exit()

print(cal_ret,"==")#[6, -200, -12] == 将获取的字符串挨个替换查找到的位置
# ret2_l = re.split((ret_list), ret_mystr)  TypeError: unhashable type: 'list' 这一步报错



            # print(re.split(k, ret_mystr))
    # sp.append(re.split((k), ret_mystr))

# print(sp)