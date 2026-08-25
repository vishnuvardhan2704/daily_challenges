class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        my_set= set(nums)
        targ=True
        i=1
        while targ==True:
            x=k*i
            if x not in my_set:
                targ!=True
                return x
            i+=1
            



        