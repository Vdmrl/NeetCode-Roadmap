import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = set(string.ascii_letters)
        for i in range(0,10):
            st.add(str(i))
        lp, rp = 0, len(s) - 1
        while rp > lp:
            while rp > lp and s[lp] not in st:
                lp += 1
            while rp > lp and s[rp] not in st:
                rp -= 1
            if s[lp].lower() != s[rp].lower():
                return False
            lp += 1
            rp -= 1
        return True
