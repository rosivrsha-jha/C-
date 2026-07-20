nums =(1,4,9,16,20,25,30,89,100,105)
idx=0
x=20
while idx<len(nums):
    if(nums[idx]==x):
     print(nums[idx])
     print("found at index",idx) 
else:
    print("founding....")
    idx+=1