from my_practice.top_k_frequent_words import Solution


def test_topKFrequent():
    sol = Solution()
    assert sol.topKFrequent(
        ["i", "love", "leetcode", "i", "love", "coding"], 2
    ) == ["i", "love"]
    assert sol.topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
         "is"], 4
    ) == ["the", "is", "sunny", "day"]
    assert sol.topKFrequent(["hello"] * 5, 1) == ["hello"]
    assert sol.topKFrequent([], 0) == []
    words = ["a", "b", "c", "a", "b", "d", "e", "d", "e", "f"]
    assert sol.topKFrequent(words, 4) == ["a", "b", "d", "e"]
    words = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
    assert sol.topKFrequent(words, 3) == [
        "apple", "banana", "cherry"
    ]
