appd_k=[]
for l in '(2*3)':
    print(l)
    if("("==l):
        l="\\"+"("
        print(l)
        appd_k.append(l)
    elif("*"==l):
        l="\\"+"*"
        appd_k.append(l)
    elif(")"==l):
        l = "\\" + ")"
        appd_k.append(l)
    else:
        print(l,"========")
        appd_k.append(l)
print(appd_k)
