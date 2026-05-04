class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for char_index in range(len(strs[0])):
            current_char = strs[0][char_index]
            for word in strs[1:]:
                if char_index >= len(word) or word[char_index] != current_char:
                    return strs[0][:char_index]
        return strs[0]







#vertical approach
# F L O W E R
# F L O W
# F L I G H T
