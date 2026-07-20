num=(1,2,3,49,50,60,70,89,49,56,50)
x=50
idx=0
for el in num:
    if(el==x):
        print("number found at idx",idx)
        break
    idx+=1