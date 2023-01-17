

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print("LazySolution:")
        indexOfValue = 1
        for i,val in enumerate(nums):
            for j in range(i+1,len(nums)):
                if val+nums[j] == target :
                    print(str(val)+"+"+str(nums[j])+",=,"+str(target)+","+str(i)+","+str(j))
                    return [i,j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print("OptimizedSolution:")
        trackedValues = {}
        for i,value in enumerate(nums):
            difference = target - value
            if difference in trackedValues:
                return [trackedValues[difference],i]
            trackedValues[value] = i                     