#Check for balanced parentheses
def is_balanced(s):
    stack=[]
    mapping={')':'(',']':'[','}':'{'}
    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack.pop()!=mapping[ch]:
                return False
    return not stack

print(is_balanced("{[()]}"))  # True
