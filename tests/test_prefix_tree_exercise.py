from my_practice.prefix_tree_exercise import find_words
from hexlet_code.helpers import build_prefix_tree
import pytest

words = [
    'apparatus',
    'apprehend',
    'appoint',
    'appreciate',
    'approachable',
    'apprentice',
    'appropriate',
    'approval',
    'appendage',
    'appraise',
    'bachelor',
    'backlash',
    'backyard',
    'baggage',
    'bailout',
    'balance',
    'ballroom',
    'bandit',
    'bankrupt',
    'barbecue',
]

tree = build_prefix_tree(words)


@pytest.mark.parametrize('prefix, expected', [
    ('appro', ['approachable', 'appropriate', 'approval']),
    ('bac', ['bachelor', 'backlash', 'backyard']),
    ('ball', ['ballroom']),
    ('appr', [
        'appraise',
        'appreciate',
        'apprehend',
        'apprentice',
        'approachable',
        'appropriate',
        'approval',
    ]),
])
def test_find_words(prefix, expected):
    assert find_words(tree, prefix) == expected
