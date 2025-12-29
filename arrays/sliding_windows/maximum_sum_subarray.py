"""
Maximum Sum Subarray of Size K

Problem:
Given an array of integers nums and an integer k, find the maximum sum of any
contiguous subarray of size k.

Example:
    Input: nums = [2, 1, 5, 1, 3, 2], k = 3
    Output: 9
    Explanation: The subarray with the maximum sum is [5, 1, 3] with a sum of 9.

Approach:
    Use sliding window technique:
    1. Calculate sum of first k elements
    2. Slide the window by removing leftmost element and adding next element
    3. Track maximum sum throughout

Time Complexity: O(n) where n is the length of nums
Space Complexity: O(1)
"""

from typing import List


def max_sum_subarray(nums: List[int], k: int) -> int:
    """
    Find the maximum sum of any contiguous subarray of size k.

    Args:
        nums: List of integers
        k: Size of the subarray

    Returns:
        Maximum sum of subarray of size k
    """
    start, curr_sum, max_sum = 0, 0, None

    for end in range(len(nums)):
        curr_sum += nums[end]
        if end - start + 1 == k:
            max_sum = max(max_sum, curr_sum) if max_sum is not None else curr_sum
            curr_sum -=  nums[start]
            start += 1
    print(max_sum)
    return max_sum


def test_max_sum_subarray():
    """Test cases for max_sum_subarray function"""

    # Test case 1: Example from problem
    assert max_sum_subarray([2, 1, 5, 1, 3, 2], 3) == 9
    print("Test 1 passed: [2, 1, 5, 1, 3, 2], k=3 -> 9")

    # Test case 2: All positive numbers
    assert max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39
    print("Test 2 passed: [1, 4, 2, 10, 23, 3, 1, 0, 20], k=4 -> 39")

    # Test case 3: Array with negative numbers
    assert max_sum_subarray([2, -1, 5, -3, 2], 2) == 4
    print("Test 3 passed: [2, -1, 5, -3, 2], k=2 -> 4")

    # Test case 4: k equals array length
    assert max_sum_subarray([1, 2, 3, 4, 5], 5) == 15
    print("Test 4 passed: [1, 2, 3, 4, 5], k=5 -> 15")

    # Test case 5: Single element window
    assert max_sum_subarray([5, 2, 9, 1, 7], 1) == 9
    print("Test 5 passed: [5, 2, 9, 1, 7], k=1 -> 9")

    # Test case 6: All negative numbers
    assert max_sum_subarray([-1, -2, -3, -4], 2) == -3
    print("Test 6 passed: [-1, -2, -3, -4], k=2 -> -3")

    # Test case 7: Mix of positive and negative
    assert max_sum_subarray([100, -200, 300, -400, 500], 2) == 100
    print("Test 7 passed: [100, -200, 300, -400, 500], k=2 -> 100")

    print("\nAll tests passed!")


if __name__ == "__main__":
    test_max_sum_subarray()