def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0


test_cases = 
    ("()", True),
    ("({[]})", True),
    ("(]", False),
    ("([)]", False),
    ("(((", False),
    (")))", False),
    ("abc(def)ghi", True),
    ("{[()]}()", True),
    ("{", False),
    ("", True),
]

for s, expected in test_cases:
    result = is_balanced(s)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: is_balanced({s!r:15}) = {result} (expected {expected})")