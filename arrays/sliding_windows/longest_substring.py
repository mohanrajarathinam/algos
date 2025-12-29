"""
Problem: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring where all characters
are distinct (no repeating characters).

Example 1:
    Input: s = "eghghhgg"
    Output: 3
    Explanation: The longest substring without repeating characters is "egh"
                 with length of 3.

Example 2:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 3:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 4:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
                 Note that "pwke" is a subsequence, not a substring.

Constraints:
    - 0 <= s.length <= 5 * 10^4
    - s consists of English letters, digits, symbols and spaces.
"""


def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.

    Args:
        s: Input string

    Returns:
        Length of the longest substring with all distinct characters
    """
    start, end, max_length = 0, 0, 0
    character_set = set()

    for end in range(len(s)):
        print(f"End is {end}")
        if s[end] not in character_set:
            character_set.add(s[end])
            print(character_set)
        else:
            while s[end] in character_set:
                character_set.remove(s[start])
                start += 1
            character_set.add(s[end])
        max_length = max(max_length, end - start + 1)
        print(f"Max is {max_length}")

    return max_length

def test_length_of_longest_substring():
    """Test cases for the longest substring problem."""

    # Test case 1: Given example
    assert length_of_longest_substring("eghghhgg") == 3, "Test case 1 failed"
    print("✓ Test case 1 passed: 'eghghhgg' -> 3")

    # Test case 2: All unique characters
    assert length_of_longest_substring("abcdefg") == 7, "Test case 2 failed"
    print("✓ Test case 2 passed: 'abcdefg' -> 7")

    # Test case 3: All same characters
    assert length_of_longest_substring("bbbbb") == 1, "Test case 3 failed"
    print("✓ Test case 3 passed: 'bbbbb' -> 1")

    # Test case 4: Repeating pattern
    assert length_of_longest_substring("abcabcbb") == 3, "Test case 4 failed"
    print("✓ Test case 4 passed: 'abcabcbb' -> 3")

    # Test case 5: Complex pattern
    assert length_of_longest_substring("pwwkew") == 3, "Test case 5 failed"
    print("✓ Test case 5 passed: 'pwwkew' -> 3")

    # Test case 6: Empty string
    assert length_of_longest_substring("") == 0, "Test case 6 failed"
    print("✓ Test case 6 passed: '' -> 0")

    # Test case 7: Single character
    assert length_of_longest_substring("a") == 1, "Test case 7 failed"
    print("✓ Test case 7 passed: 'a' -> 1")

    # Test case 8: Two characters, no repeat
    assert length_of_longest_substring("ab") == 2, "Test case 8 failed"
    print("✓ Test case 8 passed: 'ab' -> 2")

    # Test case 9: Two characters, with repeat
    assert length_of_longest_substring("aa") == 1, "Test case 9 failed"
    print("✓ Test case 9 passed: 'aa' -> 1")

    # Test case 10: Long string with spaces and symbols
    assert length_of_longest_substring("a b c a") == 3, "Test case 10 failed"
    print("✓ Test case 10 passed: 'a b c a' -> 3")

    print("\n✓ All test cases passed!")


if __name__ == "__main__":
    test_length_of_longest_substring()