class LongestPalindrome:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        res = []
        for i in range(len(s)):
            len1 = self.extendPalindrome(s,i,i)
            len2 = self.extendPalindrome(s,i,i+1)
            length = max(len1, len2)
            if length > end - start + 1:
                start = i - (length-1) // 2
                end = i + length // 2
                res.clear()
                res.append(s[start:end+1])
            elif length == end - start + 1:
                start = i - (length - 1) // 2
                end = i + length // 2
                res.append(s[start:end+1])
        return res






    def extendPalindrome(self, s, i, j):
        """
         if s is palindrome return true, otherwise return false
        """
        while(i >= 0 and j < len(s) and s[i] == s[j]):
            i -= 1
            j += 1
        return j - i - 1






def main():
    s1 = 'ababab'
    s2 = 'babadaaaaaaa'
    solu = LongestPalindrome()
    print(solu.longestPalindrome(s1))
    print(solu.longestPalindrome(s2))


if __name__ == '__main__':
    main()