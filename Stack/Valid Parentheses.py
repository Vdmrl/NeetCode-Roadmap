class Solution:
    def isValid(self, s: str) -> bool:
        # 33ms (98.33)
        # 16mb (86.71)
        if len(s) % 2 != 0:
            return False
        stack = list()
        for i in s:
            if i in {'(', '[', '{'}:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == ')' and stack[-1] != '(':
                    return False
                if i == ']' and stack[-1] != '[':
                    return False
                if i == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return not stack

    def isValidDic(self, s: str) -> bool:
        # 29 ms (99.63%)
        # 16 mb (99.15%)
        dic = {')': '(', ']': '[', '}': '{'}
        stack = list()
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i not in dic:
                stack.append(i)
                continue
            if not stack or dic[i] != stack[-1]:
                return False
            stack.pop()
        return not stack
