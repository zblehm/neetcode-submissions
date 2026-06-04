class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                try:
                    opening = stack.pop()
                    if c == ')' and opening != '(':
                        return False
                    elif c == '}' and opening != '{':
                        return False
                    elif c == ']' and opening != '[':
                        return False
                except:
                    return False

        return not bool(len(stack))
        