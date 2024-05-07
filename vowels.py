class Solution:
    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxVowels = currentVowels = 0

        for i in range(k):
            if s[i] in vowels:
                currentVowels += 1
        
        maxVowels = currentVowels

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                currentVowels -= 1
            if s[i] in vowels:
                currentVowels += 1
            maxVowels = max(maxVowels, currentVowels)

        return maxVowels


solution = Solution()
print(solution.maxVowels("abciiidef", 3)) 
print(solution.maxVowels("aeiou", 2))       
print(solution.maxVowels("leetcode", 3))   


# Author: Felipe Castro on May 7, 2024