from typing import List
class Solution:
    def wordCounter(self,words):
        word_count = {}
        for w in words:
            if w in word_count:
                word_count[w] += 1
            else:
                word_count[w] = 1
        return word_count
    
    def resetDict(self,dict,added_words):
        for w in added_words:
            dict[w] = 0

    def trimTail(self,start,jump,s,searchedWord,dict):
        word = s[start:start+jump]
        j = 0
        while word != searchedWord:
            dict[word] -= 1
            j+=1
            word = s[start+j*jump:start+(j+1)*jump]
        return j,start+j*jump
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(words[0])
        correct_indexes = []
        word_count = self.wordCounter(words)
        seen = {w:0 for w in words}
        added_words = set()
        for i in range(l):
            self.resetDict(seen,added_words)
            k = i
            #dict = {w:False for w in words}
            correct = 0
            while k <= (len(s) - l):
                word = s[k:k+l]
                if word in seen:
                    if seen[word] < word_count[word]:
                        seen[word] += 1
                        correct +=1
                        added_words.add(word)
                    ## word is in words but we already seen it correct amount of time -> this sequence is wrong, but we can continue new sequence with this word
                    else:
                        ## but we need to do it more cleverly
                        start_index = k - correct*l
                        ith_word, first_occurance = self.trimTail(start_index,l,s,word,seen)
                        correct -= ith_word
                        ## otherwise we don't do anything
                # word is not in words -> this sequence is wrong
                else:
                    correct = 0
                    self.resetDict(seen,added_words)
                # raise index k by length of word  
                k+=l
                ## update correct_indexes, first index started at k-length of words
                if correct == len(words):
                    correct_indexes.append(k-l*len(words))
                    correct -= 1
                    # now we remove first word
                    start = k-l*len(words)
                    end = start + l
                    first_word = s[start:end]
                    seen[first_word] -= 1
                    # now update set, this is little tricky, we will remove only if we seen it only 1 time. 
                    if seen[first_word] == 0:
                        added_words.remove(first_word)
        return correct_indexes

tests = [
    ("wordgoodgoodgoodbestword", ["word","good","best","good"], [8]),
    # ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
    # ("foobarfoobar", ["foo", "bar"], [0, 3, 6]),
    # ("foofoofoo", ["foo", "foo"], [0, 3]),
    # ("barbarfoo", ["bar", "bar", "foo"], [0]),
    # ("catdogcatdog", ["cat", "dog"], [0, 3, 6]),
    # ("aaaaaa", ["aa", "aa"], [0, 1, 2]),
    # ("lingmindraboofooowingdingbarrwingmonkeypoundcake",
    #  ["fooo", "barr", "wing", "ding", "wing"], [13]),
    # ("foobarfoo", ["foo", "bar"], [0, 3]),
]
solution = Solution()

for s, words, expected in tests:
    result = sorted(solution.findSubstring(s, words))
    expected = sorted(expected)

    print(
        "PASS" if result == expected else
        f"FAIL: got {result}, expected {expected}"
    )