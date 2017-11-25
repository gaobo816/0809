mystr  ='1+(2*3) - 2 * ( (60-30 +((-40/5)) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

ret_mystr =mystr.replace(' ','')
# print(ret_mystr)
import re
# print(re.search('-?\d+[*|/]\d+\)',ret_mystr).group())

#\(-?\d+[*|/]\d+\)
#\(-?\d+[*|/]\d+\)

#print(re.search('\({2}-?\d+[*|/]\d+\)',ret_mystr).group())
ret_list =  re.findall('\(-?\d+[*|/]\d+\)',ret_mystr)
cal_ret = []
for i in ret_list:

    t=i.strip("(").strip(')')
    print(t)
    ret = re.split("([*|/])",t)
    print(ret)
    # for singe_list in ret:
    #     print(singe_list[1])
    #     if("*"==singe_list[1]):
    #         cal_ret = int(singe_list[0])*int(singe_list[2])
    #     elif("/"==ret[1]):
    #         cal_ret = int(singe_list[0])*int(singe_list[2])
    #     else:
    #         print("获取的字符串有误")
    #         exit()


    if("*"==ret[1]):
        cal_ret.append(int(ret[0])*int(ret[2]))
    elif("/"==ret[1]):
        cal_ret.append(int(ret[0])*int(ret[2]))
    else:
        print("获取的字符串有误")
        exit()

print(cal_ret,"==")
