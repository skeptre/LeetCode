class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums: #loop through numbers in the list of int
            if num in count: # check if for example 1st number is in the hashmap
                count[num] += 1 
            else:
                count[num] = 1
            if count[num] > len(nums)/2:
                return num
        