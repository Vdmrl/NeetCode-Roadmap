class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(n)
        # 62ms 99%
        # 16.7mb 52%
        if len(tokens) == 1:
            return tokens[0]
        stack = []
        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                match i:
                    case "+":
                        stack[-2] = int(stack[-2]) + int(stack[-1])
                    case "-":
                        stack[-2] = int(stack[-2]) - int(stack[-1])
                    case "*":
                        stack[-2] = int(stack[-2]) * int(stack[-1])
                    case "/":
                        stack[-2] = int(stack[-2]) / int(stack[-1])
                stack.pop(-1)
            else:
                stack.append(i)
        return int(stack[-1])