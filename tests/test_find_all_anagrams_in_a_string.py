from my_practice.find_all_anagrams_in_a_string import Solution


def test_find_all_anagrams():
    solution = Solution()
    assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert solution.findAnagrams("abab", "ab") == [0, 1, 2]
    assert solution.findAnagrams("abcdefg", "xyz") == []
    assert solution.findAnagrams("", "a") == []
    assert solution.findAnagrams("abcdefg", "") == []
    assert solution.findAnagrams("abc", "abcd") == []
    assert solution.findAnagrams("a", "a") == [0]
    assert solution.findAnagrams("a", "b") == []
    assert solution.findAnagrams("abcba", "bca") == [0, 2]
    assert solution.findAnagrams("aaa", "aa") == [0, 1]
    assert solution.findAnagrams("anagram", "nagaram") == [0]
