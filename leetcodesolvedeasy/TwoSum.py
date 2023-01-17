class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        indexOfValue = 1
        for i,val in enumerate(nums):
            for j in range(i+1,len(nums)):
                if val+nums[j] == target :
                    print(str(val)+"+"+str(nums[j])+",=,"+str(target)+","+str(i)+","+str(j))
                    return [i,j]