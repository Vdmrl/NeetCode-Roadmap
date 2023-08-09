class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 45ms 99%
        # 16mb 98%
        st = set()
        max_length = 0
        j = 0
        for i in s:
            while i in st:
                st.remove(s[j])
                j += 1
            st.add(i)
            max_length = max(max_length, len(st))
        return max_length
