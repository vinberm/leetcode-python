class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        lens = 0
        smap = {}
        for j in range(len(s)):
            if s[j] in smap:
                i = max(smap[s[j]], i)
            lens = max(lens, j-i+1)
            smap[s[j]] = j+1
        return lens



def main():
    s = "aaaaaabgaa"
    solu = Solution()
    result = solu.lengthOfLongestSubstring(s)
    print(result)
    # assert result == 2

if __name__ == '__main__':
    main()