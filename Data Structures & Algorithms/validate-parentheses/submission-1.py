class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for c in s:
            if c == "(":
                stack.append("(")
            if c == "{":
                stack.append("{")
            if c == "[":
                stack.append("[")
            if c == ")":
                if len(stack) == 0:
                    return False
                res = stack.pop()
                if res != "(":
                    return False
            if c == "}":
                if len(stack) == 0:
                    return False
                res = stack.pop()
                if res != "{":
                    return False
            if c == "]":
                if len(stack) == 0:
                    return False
                res = stack.pop()
                if res != "[":
                    return False
        if len(stack) != 0:
            return False
        return True

            