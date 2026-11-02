from solve import Solution

tests = [
    # (s, p, expected)
    ("aa", "a", False),
    ("aa", "*", True),
    ("cb", "?a", False),
    ("", "", True),
    ("", "*", True),
    ("", "?", False),
    ("a", "a?", False),
    ("ab", "a?", True),
    ("a", "a*", True),
    ("ba", "*a", True),
    ("ab", "*a", False),
    ("adceb", "*a*b", True),
    ("acdcb", "a*c?b", False),
]

sol = Solution()
for s, p, expected in tests:
    result = sol.isMatch(s, p)
    status = "OK" if result == expected else "FAIL"
    print(f"{status}: s={s!r}, p={p!r}, expected={expected}, got={result}")