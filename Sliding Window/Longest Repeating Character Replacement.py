from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 96 ms 90%
        # 16.3mb 96%
        st = defaultdict(int)
        max_ans = 1
        l = 0
        for r in range(len(s)):
            st[s[r]] += 1
            if (r - l + 1) - max(st.values()) > k:
                st[s[l]] -= 1
                l += 1
            else:
                max_ans = max(sum(st.values()), max_ans)
        return max_ans

    def characterReplacementMaxF(self, s: str, k: int) -> int:
        # 83 ms 96%
        # 16.4mb 76%
        st = defaultdict(int)
        max_ans = 1
        l = 0
        max_f = 0
        for r in range(len(s)):
            st[s[r]] += 1
            max_f = max(max_f, st[s[r]])
            if (r - l + 1) - max_f > k:
                st[s[l]] -= 1
                l += 1
            else:
                max_ans = max(sum(st.values()), max_ans)
        return max_ans


Solution().characterReplacement("ABAB", 2)
