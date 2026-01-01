class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        def reverse_in_place(left,right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse_in_place(0, n-1)
        reverse_in_place(0, k-1)
        reverse_in_place(k, n-1)
        """
        Do not return anything, modify nums in-place instead.
        """
        
# We wrote a helper function to reverse the whole array using while loop and 2 pointers. 
# We called the function and reverse the whole array first from 0 to n-1
# We reverse the first part (k elements).
# The modulo operation k % n ensures efficiency by reducing any rotation value k greater than the array length n to its effective remainder, preventing redundant "full-circle" rotations and keeping index calculations within memory bounds.
# After reversing the whole, we reverst just the first part and then the second part
# If no work is needed, the modulo logic explained above saves us unnecessary work
