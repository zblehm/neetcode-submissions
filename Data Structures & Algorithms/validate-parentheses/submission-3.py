class Solution:
    def isValid(self, s: str) -> bool:
        closing_characters = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            # check if closing characters match the top of the stack
            if c in closing_characters.values():
                # make sure there are opening characters to check against
                if len(stack) == 0:
                    return False
                else:
                    opening = stack.pop()
                    # if the closing character does not match top of the stack return False
                    if c != closing_characters[opening]:
                        return False
            # add non-closing characters to the stack
            else:
                stack.append(c)
        # if stack is empty everything matches, return True else False
        return not bool(len(stack))
        