class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]       
        return i+1
            
        
        
# if list is empty return 0, no items or duplicates
# first pointer set to 0 -> i=0
# we loop using second (fast pointer) from range 1 to len of nums
# now we should check if an int in the looping session does not match first pointer, that means we have reached a non duplicate so a new number
#now that we have reached this new number which is not a duplicate but different from slow pointer, we can increment the slow pointer by 1 and then overwrite it with the number found.
#by doing the above, we are modifying the in place list and moving unique integers in the beginning
#overwriting i think makes the time complexity O(n) rather than moving elements throughout which would or could be an O(n^2)
# once the looping is finished, at the end if the function, we can return slow pointer + 1 because of index 0