class Solution(object):

    def longestPalindrome(self, s):

        l = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

        l = [x for x in l if x == x[::-1]]
        a = sorted(l,key=len) 
        return a[-1]


obj = Solution()
print(obj.longestPalindrome("cbbd"))