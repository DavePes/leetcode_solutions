class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.matching(s,p,0,0)
    # si, pi indexes in s and p
    def matching(self,s,p,si,pi,cache = None):
        if cache is None:
            cache = {}
        if (si,pi) in cache:
            return cache[(si,pi)]
        if (len(s) == si and len(p) == pi):
            cache[(si,pi)] = True
            return True
        if len(p) <= pi:
            cache[(si,pi)] = False
            return False
        
        # handle '*' wildcard branch.
        # len(p) - pi > 1 ensures p[pi + 1] is within bounds
        if len(p) - pi > 1 and p[pi+1] == '*':
            # either we skip entire p[pi:pi+2] (the letter and the '*')
            if self.matching(s,p,si,pi+2,cache) == True:
                cache[(si,pi)] = True
                return True
            matched_letter = p[pi]
            # or we match one or more letters in s with p[pi]
            while si < len(s) and (s[si] == matched_letter or matched_letter == '.'):
                if self.matching(s,p,si+1,pi+2,cache) == True:
                    cache[(si,pi)] = True
                    return True
                si+=1
            cache [(si,pi)] = False
        # match a single character (literal or '.' wildcard) without a '*' follower
        else:
            if (si < len(s) and s[si] == p[pi]) or p[pi] == '.':
                cache[(si,pi)] = self.matching(s,p,si+1,pi+1,cache)
            else:
                cache[(si,pi)] = False
        return cache[(si,pi)]



tests = [
    ("aa", "a", False),                 ("aa", "a*", True),
    ("ab", ".*", True),                 ("", "", True),
    ("", "a*b*c*", True),               ("a", "", False),
    ("aab", "c*a*b", True),             ("aabbcc", "a*b*c*", True),
    ("aabbcc", "a*c*b*", False),        ("ab", ".*.*.*", True),
    ("aaa", "a*a*a*a", True),           
    ("aaa", "a*a*a*a*b", False),
    ("aaba", "a*b*a*b*a", True),        
    ("aabb", "a*b*a*b*a", False),
    ("bbbba", ".*a*a", True),           
    ("ac", "ab*c", True),
    ("abbbc", "ab*c", True),            
    ("xyz", "x*y*z*x*y*z*", True),
    ("abcdef", ".*.*f", True),          
    ("abcdef", ".*.*z", False),
    ("mississippi", "mis*is*p*.", False), 
    ("mississippi", "mis*is*ip*.", True),
]

sol, bad = Solution(), 0
for s, p, want in tests:
    got = sol.isMatch(s, p)
    ok = got == want
    bad += not ok
    print(f"{'ok  ' if ok else 'FAIL'} s={s!r:<14} p={p!r:<16} want={want!s:<5} got={got}")
print(f"\n{len(tests)-bad}/{len(tests)} passed —", "ALL CORRECT" if not bad else f"{bad} WRONG")