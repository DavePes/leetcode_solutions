
def recursWavi(s, idx, prev_prev, prev, is_tight, is_started, cache):
    if idx == len(s):
        return (1, 0)
    state = (idx, prev_prev, prev, is_tight, is_started)
    if state in cache:
        return cache[state]
    max = int(s[idx]) if is_tight else 9
    for i in range(max):
        if not is_started and i == 0:
            res = recursWavi(s, idx + 1, prev_prev, prev, s[idx] == str(i), False, cache)
        else:
            res = recursWavi(s, idx + 1, prev, i, s[idx] == str(i), True, cache)
     

def totalWaviness(self, num1: int, num2: int) -> int:
    cache = {}
    a = recursWavi(num2,cache)


    


