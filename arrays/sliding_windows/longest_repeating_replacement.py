"""
Longest Repeating Character Replacement

Problem:
Given a string s and an integer k, find the length of the longest substring containing
the same letter after performing at most k operations where you can change any character
to any other uppercase English letter.

Example:
Input: s = "BBABCCDD", k = 2
Output: 5
Explanation: Replace the first 'A' and 'C' with 'B' to form "BBBBBCDD".
The longest substring with identical letters is "BBBBB", which has a length of 5.

Approach:
- Use sliding window technique
- Track the character with maximum frequency in the current window
- If (window_length - max_frequency) > k, shrink the window from left
- The answer is the maximum window size we can achieve
"""


def characterReplacement(s: str, k: int) -> int:
    """
    Find the length of the longest substring with same characters after at most k replacements.

    Args:
        s: Input string containing uppercase English letters
        k: Maximum number of character replacements allowed

    Returns:
        Length of the longest substring with identical letters
    """
    start, end, max_length = 0, 0, 0
    freq = {}
    max_frequency = 0

    for end in range(len(s)):
        freq[s[end]] = freq.get(s[end], 0) + 1
        max_frequency = max(max_frequency, freq[s[end]])

        if k + max_frequency < end - start + 1:
            freq[s[start]] -= 1
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


def test_characterReplacement():
    """Test cases for the characterReplacement function"""

    # Test case 1: Example from problem statement
    assert characterReplacement("BBABCCDD", 2) == 5, "Test case 1 failed"
    print("Test case 1 passed: s='BBABCCDD', k=2 -> 5")

    # Test case 2: All same characters
    assert characterReplacement("AAAA", 0) == 4, "Test case 2 failed"
    print("Test case 2 passed: s='AAAA', k=0 -> 4")

    # Test case 3: Classic example
    assert characterReplacement("AABABBA", 1) == 4, "Test case 3 failed"
    print("Test case 3 passed: s='AABABBA', k=1 -> 4")

    # Test case 4: Need all replacements
    assert characterReplacement("ABAB", 2) == 4, "Test case 4 failed"
    print("Test case 4 passed: s='ABAB', k=2 -> 4")

    # Test case 5: Single character
    assert characterReplacement("A", 1) == 1, "Test case 5 failed"
    print("Test case 5 passed: s='A', k=1 -> 1")

    # Test case 6: Longer string with multiple replacements
    assert characterReplacement("AABABBAB", 2) == 6, "Test case 6 failed"
    print("Test case 6 passed: s='AABABBAB', k=2 -> 6")

    # Test case 7: No replacements needed
    assert characterReplacement("ABCDE", 0) == 1, "Test case 7 failed"
    print("Test case 7 passed: s='ABCDE', k=0 -> 1")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_characterReplacement()