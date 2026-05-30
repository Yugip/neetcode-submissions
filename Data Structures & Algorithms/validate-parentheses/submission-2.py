class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openB = "([{"
        
        for i in range(len(s)):
            print(s[i])
            if s[i] in openB:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    o = stack.pop()

                    if s[i] == ")" and o == "(":
                        continue

                    elif s[i] == "}" and o == "{":
                        continue

                    elif s[i] == "]" and o == "[":
                        continue
                    
                    else:
                        return False

        if len(stack) == 0:
            return True
        else:
            return False