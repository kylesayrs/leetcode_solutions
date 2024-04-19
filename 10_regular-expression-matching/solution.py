from typing import Tuple, List


class Solution:
    def unzip_pattern_stars(pattern: str) -> Tuple[str, List[bool]]:
        p = []
        stars = []

        for char in pattern:
            if char != "*":
                p.append(char)
                stars.append(False)
            
            else:
                stars[-1] = True

        return "".join(p), stars
    

    def matches(s_char, p_char):
        return s_char == p_char or p_char == "."


    def isMatch(self, s: str, p: str) -> bool:
        p, stars = Solution.unzip_pattern_stars(p)
        cache = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]

        # string can never match with empty pattern
        for string_index in range(len(s)):
            cache[string_index][-1] = False

        # empty string can always match with empty string
        cache[-1][-1] = True

        # pattern can only match with empty string if star and right matches
        for pattern_index in reversed(range(len(p))):
            cache[-1][pattern_index] = True if stars[pattern_index] and cache[-1][pattern_index + 1] else False

        for string_index in reversed(range(len(s))):
            for pattern_index in reversed(range(len(p))):
                if stars[pattern_index]:
                    none_matches = cache[string_index][pattern_index + 1]
                            
                    some_matches = (
                        cache[string_index + 1][pattern_index]
                        if Solution.matches(s[string_index], p[pattern_index])
                        else False
                    )
                    
                    cache[string_index][pattern_index] = none_matches or some_matches

                else:  # p[pattern_index] is alpha or .
                    cache[string_index][pattern_index] = (
                        cache[string_index + 1][pattern_index + 1]
                        if Solution.matches(s[string_index], p[pattern_index])
                        else False
                    )

        #import numpy; print(numpy.array(cache))
        return cache[0][0]


if __name__ == "__main__":
    assert Solution.unzip_pattern_stars("asdf") == ("asdf", [False, False, False, False])
    assert Solution.unzip_pattern_stars("a*sdf") == ("asdf", [True, False, False, False])
    assert Solution.unzip_pattern_stars("asd*f") == ("asdf", [False, False, True, False])
    assert Solution.unzip_pattern_stars("asdf*") == ("asdf", [False, False, False, True])

    assert Solution().isMatch("asdf", "asdf") == True
    assert Solution().isMatch("asdf", "asdf*") == True
    assert Solution().isMatch("asdf", "a*sdf") == True
    assert Solution().isMatch("aaaaaaasdf", "a*sdf") == True
    assert Solution().isMatch("sdf", "a*sdf") == True
    assert Solution().isMatch("sdf", "a*sd*f") == True
    assert Solution().isMatch("sddddddddf", "a*sd*f") == True
    assert Solution().isMatch("sddddddddf", "a*sd*f") == True
    assert Solution().isMatch("sddddddddf", "a*sd*g") == False
    assert Solution().isMatch("sdddddddd", "a*sd*g*") == True
    assert Solution().isMatch("sddddddddf", "a*sd*g*") == False

    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aaaaa", "a") == False
    assert Solution().isMatch("aaaaa", "aaaaaaaaaaaa") == False
    assert Solution().isMatch("aaaaab", "aaaaaaaaaaaab") == False
    assert Solution().isMatch("baaaaa", "baaaaaaaaaaab") == False

    assert Solution().isMatch("asdfasdfasdfasdfasdf", ".*") == True
    assert Solution().isMatch("ab", "a*") == False
    assert Solution().isMatch("abbb", "a*b*") == True

    assert Solution().isMatch("ab", ".*c") == False
