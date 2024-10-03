from my_practice.group_anagrams import Solution


def test_group_anagrams():
    solution = Solution()
    expected_result = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

    assert sorted([sorted(group) for group in result]) == sorted(
        [sorted(group) for group in expected_result])
    assert sorted(solution.groupAnagrams([""])) == [[""]]
    assert sorted(solution.groupAnagrams(["a"])) == [["a"]]

    expected_result = [["abc", "bca", "cab"], ["xyz", "yxz"]]
    result = solution.groupAnagrams(["abc", "bca", "cab", "xyz", "yxz"])

    assert sorted([sorted(group) for group in result]) == sorted(
        [sorted(group) for group in expected_result])

    expected_result = [["apple"], ["pale", "leap", "plea"], ["hello"]]
    result = solution.groupAnagrams(["apple", "pale", "leap", "plea", "hello"])

    assert sorted([sorted(group) for group in result]) == sorted(
        [sorted(group) for group in expected_result])
