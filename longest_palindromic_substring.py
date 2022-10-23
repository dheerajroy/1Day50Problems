"""Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        subsets = []
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if j > i:
                    subsets.append(s[i:j])
                
        outputs = sorted(set(filter(lambda x: x == x[::-1], subsets)), key=len, reverse=True)
        return outputs[0]

if __name__ == '__main__':
    print(Solution().longestPalindrome(s='babad'))
