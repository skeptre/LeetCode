class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word1 = {}
        word2 = {}
        for i in range(len(s)):
            word1[s[i]] = word1.get(s[i], 0) + 1
        for j in range(len(t)):
            word2[t[j]] = word2.get(t[j], 0) + 1
        
        return word1 == word2
