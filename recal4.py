mystr  ='1+(2*3) - 2 * ( (60-30 +((-40/5)) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

ret_mystr =mystr.replace(' ','')
ret_mystr2 =mystr.replace(' ','')
import re
# my_re = '\(-?\d+[*|/]\d+\)'
ret_list =  re.findall('\(-?\d+[*|/]\d+\)',ret_mystr)
print('ret_list',ret_list)
cal_ret = []
for i in ret_list:

    t=i.strip("(").strip(')')
    # print(t)
    ret = re.split("([*|/])",t)
    # print(ret)
    if("*"==ret[1]):
        cal_ret.append(int(ret[0])*int(ret[2]))
    elif("/"==ret[1]):
        cal_ret.append(int(ret[0])*int(ret[2]))
    else:
        print("获取的字符串有误")
        exit()

for k in range(len(ret_list)):
    print(ret_list[k], str(cal_ret[k]),"================")
    ret_mystr=ret_mystr.replace(ret_list[k], str(cal_ret[k]))


print(ret_mystr)

if('--'.find(ret_mystr)):
    ret_mystr = ret_mystr.replace('--','+')
    print(ret_mystr)
#
# my_re = r'(\d+([-|+|*|/]\d+)+)'
ret_list =  re.findall('\([^(]*?\)',ret_mystr)

print('ret_list',ret_list)
cal_ret=""
for i in ret_list:

    print(i)

    tt = re.match('\d[*|/]\d',i)
