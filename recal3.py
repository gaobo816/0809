mystr  ='1+(2*3) - 2 * ( (60-30 +((-40/5)) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

ret_mystr =mystr.replace(' ','')
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

# print(cal_ret,"==")#[6, -200, -12] == 将获取的字符串挨个替换查找到的位置
# mystr_new=""
# for j in range(len(ret_list)):
#     print(type(ret_list[j]))
#     print(ret_list[j],cal_ret[j],"==============")
#     ret_mystr.replace(ret_list[j],str(cal_ret[j]))
# tt=ret_list[0]
# print("ttt",tt)
# ret_list[0] ='(2*3)'
# print(ret_list[0],"==============")
# if(tt==ret_list[0]):
#     print("00000")
# print(len(ret_list),len(cal_ret))
# for i in range(len(ret_list)):
# ret_mystr=ret_mystr.replace(ret_list[0],str(cal_ret[0]))
# print(ret_list[0],str(cal_ret[0]))
# ret_mystr=ret_mystr.replace(ret_list[1],str(cal_ret[1]))
# print(ret_list[1],str(cal_ret[1]))
# ret_mystr=ret_mystr.replace(ret_list[2],str(cal_ret[2]))
# print(ret_list[2],str(cal_ret[2]))
# ret_mystr1=ret_mystr.replace('(2*3)','tt')
# print(ret_mystr)

for k in range(len(ret_list)):
    print(ret_list[k], str(cal_ret[k]),"================")
    ret_mystr=ret_mystr.replace(ret_list[k], str(cal_ret[k]))


print(ret_mystr)

if('--'.find(ret_mystr)):
    ret_mystr = ret_mystr.replace('--','+')
    print(ret_mystr)

my_re = r'(\d+([-|+|*|/]\d+)+)'
ret_list =  re.findall(my_re,ret_mystr)

print('ret_list',ret_list)
#正则表达式可以用
# \(\d+[-|+|*|/]

