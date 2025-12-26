"""
3Sum Problem

Given an input integer array nums, find all unique triplets [nums[i], nums[j], nums[k]]
such that i, j, and k are distinct indices, and the sum of nums[i], nums[j], and nums[k]
equals zero. Ensure that the resulting list does not contain any duplicate triplets.

Time Complexity: O(n²) - Sorting takes O(n log n), outer loop runs n times,
                       and inner two-pointer traversal is O(n) for each iteration
Space Complexity: O(1) or O(n) - O(1) extra space (ignoring output list),
                       but O(n) if considering the space used by sorting algorithm
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets in the array that sum to zero.

    Args:
        nums: List of integers

    Returns:
        List of unique triplets that sum to zero

    Example:
        >>> three_sum([-1, 0, 1, 2, -1, -1])
        [[-1, -1, 2], [-1, 0, 1]]
    """
    # Sort the array to enable two-pointer approach and handle duplicates easily
    nums.sort()
    solution = list()

    # Iterate through array, fixing the first element of the triplet
    # Stop at len(nums) - 2 since we need at least 3 elements
    for i in range(len(nums) - 2):
        # Skip duplicate values for the first element to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Initialize two pointers for the remaining elements
        left = i + 1
        right = len(nums) - 1

        # Use two-pointer technique to find pairs that sum with nums[i] to zero
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                # Sum is too small, move left pointer right to increase sum
                left += 1
            elif total > 0:
                # Sum is too large, move right pointer left to decrease sum
                right -= 1
            else:
                # Found a valid triplet that sums to zero
                solution.append([nums[i], nums[left], nums[right]])

                # Skip duplicate values for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicate values for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers to continue searching for other triplets
                left += 1
                right -= 1

    return solution

def test_three_sum():
    """Test cases for the 3Sum problem."""

    # Test case 1: Basic example from problem statement
    nums = [-1, 0, 1, 2, -1, -1]
    result = three_sum(nums)
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted(result) == sorted(expected), f"Test 1 failed: Expected {expected}, got {result}"
    print("✓ Test 1 passed: Basic example")

    # Test case 2: Empty array
    nums = []
    result = three_sum(nums)
    expected = []
    assert result == expected, f"Test 2 failed: Expected {expected}, got {result}"
    print("✓ Test 2 passed: Empty array")

    # Test case 3: Array with less than 3 elements
    nums = [0, 1]
    result = three_sum(nums)
    expected = []
    assert result == expected, f"Test 3 failed: Expected {expected}, got {result}"
    print("✓ Test 3 passed: Less than 3 elements")

    # Test case 4: All zeros
    nums = [0, 0, 0]
    result = three_sum(nums)
    expected = [[0, 0, 0]]
    assert result == expected, f"Test 4 failed: Expected {expected}, got {result}"
    print("✓ Test 4 passed: All zeros")

    # Test case 5: Multiple zeros
    nums = [0, 0, 0, 0]
    result = three_sum(nums)
    expected = [[0, 0, 0]]
    assert result == expected, f"Test 5 failed: Expected {expected}, got {result}"
    print("✓ Test 5 passed: Multiple zeros (no duplicates)")

    # Test case 6: No solution
    nums = [1, 2, 3]
    result = three_sum(nums)
    expected = []
    assert result == expected, f"Test 6 failed: Expected {expected}, got {result}"
    print("✓ Test 6 passed: No solution exists")

    # Test case 7: Negative numbers only
    nums = [-1, -2, -3, -4]
    result = three_sum(nums)
    expected = []
    assert result == expected, f"Test 7 failed: Expected {expected}, got {result}"
    print("✓ Test 7 passed: All negative numbers")

    # Test case 8: Positive numbers only
    nums = [1, 2, 3, 4]
    result = three_sum(nums)
    expected = []
    assert result == expected, f"Test 8 failed: Expected {expected}, got {result}"
    print("✓ Test 8 passed: All positive numbers")

    # Test case 9: Multiple solutions
    nums = [-2, 0, 1, 1, 2]
    result = three_sum(nums)
    expected = [[-2, 0, 2], [-2, 1, 1]]
    assert sorted(result) == sorted(expected), f"Test 9 failed: Expected {expected}, got {result}"
    print("✓ Test 9 passed: Multiple solutions")

    # Test case 10: Duplicates in input
    nums = [-4, -1, -1, 0, 1, 2]
    result = three_sum(nums)
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted(result) == sorted(expected), f"Test 10 failed: Expected {expected}, got {result}"
    print("✓ Test 10 passed: Duplicates in input")

    # Test case 11: Large array with multiple solutions
    nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    result = three_sum(nums)
    # Should have multiple valid triplets
    assert len(result) > 0, f"Test 11 failed: Expected solutions, got {result}"
    # Verify all triplets sum to zero
    for triplet in result:
        assert sum(triplet) == 0, f"Test 11 failed: Triplet {triplet} doesn't sum to 0"
    print(f"✓ Test 11 passed: Large array with {len(result)} solutions")

    # Test case 12: Array with many duplicates
    nums = [0, 0, 0, 0, 0]
    result = three_sum(nums)
    expected = [[0, 0, 0]]
    assert result == expected, f"Test 12 failed: Expected {expected}, got {result}"
    print("✓ Test 12 passed: Many duplicate zeros")

    # Test case 13: Single solution
    nums = [-1, 0, 1]
    result = three_sum(nums)
    expected = [[-1, 0, 1]]
    assert result == expected, f"Test 13 failed: Expected {expected}, got {result}"
    print("✓ Test 13 passed: Single solution")

    # Test case 14: Mix of positive, negative, and zeros
    nums = [-3, 0, 1, 2, -1, 1, -2]
    result = three_sum(nums)
    # Verify no duplicates in result
    result_tuples = [tuple(sorted(triplet)) for triplet in result]
    assert len(result_tuples) == len(set(result_tuples)), "Test 14 failed: Duplicate triplets found"
    # Verify all sum to zero
    for triplet in result:
        assert sum(triplet) == 0, f"Test 14 failed: Triplet {triplet} doesn't sum to 0"
    print(f"✓ Test 14 passed: Mixed numbers with {len(result)} unique solutions")

    # Test case 15: Edge case with exact 3 elements
    nums = [-2, 1, 1]
    result = three_sum(nums)
    expected = [[-2, 1, 1]]
    assert result == expected, f"Test 15 failed: Expected {expected}, got {result}"
    print("✓ Test 15 passed: Exact 3 elements")

    print("\n" + "="*50)
    print("All tests passed! 🎉")
    print("="*50)


if __name__ == "__main__":
    test_three_sum()