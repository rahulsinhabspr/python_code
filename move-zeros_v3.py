# -*- coding: utf-8 -4
"""
Created on Tue Oct  3 13:43:10 2023

@author: rahul
"""
nums = [0,1,0,3,12]
print(nums)
print(nums.count(0))
for i in range(len(nums)-1):
        print('loop seq',i)
        temp = nums[i]
        print('temp',i,temp)
        if nums[i] == 0:
            for j in range(i,len(nums)):
                if nums[j] != 0:
                    print('innerloop',j)
                    print('innerloop',nums[j])
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
         
print(nums)
        
    
    