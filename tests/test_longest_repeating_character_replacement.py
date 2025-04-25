from my_practice.longest_repeating_character_replacement import Solution


def test_character_replacement():
    s = Solution()
    assert s.characterReplacement("ABAB", 2) == 4
    assert s.characterReplacement("AABABBA", 1) == 4
    assert s.characterReplacement("AAAA", 2) == 4
    assert s.characterReplacement("ABCDE", 1) == 2
