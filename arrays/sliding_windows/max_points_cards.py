"""
Maximum Points You Can Obtain from Cards

Problem Statement:
-----------------
Given an array of integers representing the value of cards, write a function to calculate
the maximum score you can achieve by selecting exactly k cards from either the beginning
or the end of the array.

For example, if k = 3, then you have the option to select:
- the first three cards
- the last three cards
- the first card and the last two cards
- the first two cards and the last card

Example 1:
----------
Input:
    cards = [2, 11, 4, 5, 3, 9, 2]
    k = 3
Output:
    17
Explanation:
    - Selecting the first three cards from the beginning (2 + 11 + 4) gives a total of 17.
    - Selecting the last three cards (3 + 9 + 2) gives a total of 14.
    - Selecting the first card and the last two cards (2 + 9 + 2) gives a total of 13.
    - Selecting the first two cards and the last card (2 + 11 + 2) gives a total of 15.
    So the maximum score is 17.

Constraints:
------------
- 1 <= cards.length <= 10^5
- 1 <= k <= cards.length
- 1 <= cards[i] <= 10^4

Approach:
---------
Use a sliding window technique to calculate all possible combinations of selecting
i cards from the beginning and (k-i) cards from the end, where i ranges from 0 to k.
"""


def max_score(cards: list[int], k: int) -> int:
    """
    Calculate the maximum score by selecting exactly k cards from either end.

    Args:
        cards: List of integers representing card values
        k: Number of cards to select
        e.g., [2, 11, 4, 5, 3, 9, 2]
    Returns:
        Maximum possible score
    """
    length = len(cards)

    start = length - k
    curr_sum = sum(cards[length - k:])
    max_sum = curr_sum
    print(f"initial_sum = {curr_sum}")
    for card in cards[:k]:
        curr_sum = curr_sum + card
        curr_sum = curr_sum - cards[start]
        start += 1
        max_sum = max(max_sum, curr_sum)
    return max_sum


def test_max_score():
    """Test cases for the max_score function."""

    # Test case 1: Example from problem statement
    cards1 = [2, 11, 4, 5, 3, 9, 2]
    k1 = 3
    expected1 = 17
    result1 = max_score(cards1, k1)
    assert result1 == expected1, f"Test 1 Failed: Expected {expected1}, got {result1}"
    print(f"✓ Test 1 Passed: cards={cards1}, k={k1}, result={result1}")

    # Test case 2: Select all cards from beginning
    cards2 = [1, 2, 3, 4, 5, 6, 1]
    k2 = 3
    expected2 = 12  # 1 + 2 + 3 = 6 vs 6 + 1 + 5 = 12 (last 3)
    result2 = max_score(cards2, k2)
    assert result2 == expected2, f"Test 2 Failed: Expected {expected2}, got {result2}"
    print(f"✓ Test 2 Passed: cards={cards2}, k={k2}, result={result2}")

    # Test case 3: Single card
    cards3 = [100]
    k3 = 1
    expected3 = 100
    result3 = max_score(cards3, k3)
    assert result3 == expected3, f"Test 3 Failed: Expected {expected3}, got {result3}"
    print(f"✓ Test 3 Passed: cards={cards3}, k={k3}, result={result3}")

    # Test case 4: All cards must be selected
    cards4 = [9, 7, 7, 9, 7, 7, 9]
    k4 = 7
    expected4 = 55  # Sum of all cards
    result4 = max_score(cards4, k4)
    assert result4 == expected4, f"Test 4 Failed: Expected {expected4}, got {result4}"
    print(f"✓ Test 4 Passed: cards={cards4}, k={k4}, result={result4}")

    # Test case 5: Optimal selection from both ends
    cards5 = [1, 79, 80, 1, 1, 1, 200, 1]
    k5 = 3
    expected5 = 202  # 1 + 1 + 200 (last 3)
    result5 = max_score(cards5, k5)
    assert result5 == expected5, f"Test 5 Failed: Expected {expected5}, got {result5}"
    print(f"✓ Test 5 Passed: cards={cards5}, k={k5}, result={result5}")

    # Test case 6: Mixed selection
    cards6 = [96, 90, 41, 82, 39, 74, 64, 50, 30]
    k6 = 8
    expected6 = 536  # Sum of all except one element (30 is smallest to exclude)
    result6 = max_score(cards6, k6)
    assert result6 == expected6, f"Test 6 Failed: Expected {expected6}, got {result6}"
    print(f"✓ Test 6 Passed: cards={cards6}, k={k6}, result={result6}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_max_score()