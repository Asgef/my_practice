from my_practice.partition_labels import Solution


def test_partition_labels():
    solution = Solution()
    assert solution.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert solution.partitionLabels("eccbbbbdec") == [10]
    assert solution.partitionLabels("ababcc") == [4, 2]
    assert solution.partitionLabels("a") == [1]
    assert solution.partitionLabels("abcde") == [1, 1, 1, 1, 1]
