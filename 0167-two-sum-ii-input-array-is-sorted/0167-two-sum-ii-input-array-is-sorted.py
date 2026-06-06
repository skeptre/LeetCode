class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while right > left:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right = right -1
            elif sum < target:
                left = left +1
            elif sum == target:
                return left+1, right+1