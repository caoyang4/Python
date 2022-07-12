class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = 0
        if needle == "":
            return index
        if len(haystack) < len(needle):
            return -1
        diff = len(haystack) - len(needle)
        original = haystack
        while (not haystack.startswith(needle)) and len(haystack) >= len(needle):
            index += 1
            haystack = original[index:]
        return index if index <= diff else -1

print(Solution().strStr("abc", "c"))