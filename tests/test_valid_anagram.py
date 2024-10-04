from my_practice.valid_anagram import Solution


def test_valid_anagram():
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram") is True
    assert solution.isAnagram("rat", "car") is False
    assert solution.isAnagram("listen", "silent") is True
    assert solution.isAnagram("apple", "pale") is False
    assert solution.isAnagram("aabbcc", "ccbbaa") is True
    assert solution.isAnagram("", "") is True
