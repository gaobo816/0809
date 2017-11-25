mystr  ='1+(2*3) - 2 * ( (60-30 +((-40/5)) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
ret_mystr =mystr.replace(' ','')

import re
ret_mystr =ret_mystr.replace('(2*3)','200')
print(ret_mystr)
