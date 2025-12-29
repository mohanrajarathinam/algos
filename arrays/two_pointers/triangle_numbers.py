"""
Triangle Numbers

Problem:
Write a function to count the number of triplets in an integer array nums that could
form the sides of a triangle. For three sides to form a valid triangle, the sum of any
two sides must be greater than the third side. The triplets do not need to be unique.

Triangle Inequality Theorem:
For three sides a, b, c to form a valid triangle:
- a + b > c
- b + c > a
- a + c > b

Example 1:
Input: nums = [11, 4, 9, 6, 15, 18]
Output: 10
Explanation: Valid combinations are:
    4, 6, 9
    4, 9, 11
    4, 11, 15
    4, 15, 18
    6, 9, 11
    6, 11, 15
    6, 15, 18
    9, 11, 15
    9, 15, 18
    11, 15, 18

Constraints:
- 3 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
"""

from typing import List


def triangle_number(nums: List[int]) -> int:
    """
    Count the number of triplets that can form valid triangles.

    Args:
        nums: List of integers representing potential triangle sides

    Returns:
        int: Number of valid triangle triplets
    """
    nums.sort()
    count = 0
    """
    [1,1,3,4,5,7,9]
    """
    for i in range(len(nums)-1, 1 , -1):
        left, right = 0, i-1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += right - left
                right -= 1
            else:
                left += 1

    return count


def test_triangle_number():
    """Test cases for triangle_number function"""

    # Test case 1: Example from problem
    nums1 = [11, 4, 9, 6, 15, 18]
    expected1 = 10
    result1 = triangle_number(nums1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print(f"Test 1 passed: {nums1} -> {result1}")

    # Test case 2: Minimum input
    nums2 = [2, 2, 3]
    expected2 = 1
    result2 = triangle_number(nums2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"Test 2 passed: {nums2} -> {result2}")

    # Test case 3: No valid triangles
    nums3 = [1, 2, 10]
    expected3 = 0
    result3 = triangle_number(nums3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"Test 3 passed: {nums3} -> {result3}")

    # Test case 4: All same values
    nums4 = [5, 5, 5, 5]
    expected4 = 4  # All combinations of 3 from 4 identical values
    result4 = triangle_number(nums4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"Test 4 passed: {nums4} -> {result4}")

    # Test case 5: Sequential numbers
    nums5 = [1, 2, 3, 4, 5]
    expected5 = 3  # (2,3,4), (2,4,5), (3,4,5)
    result5 = triangle_number(nums5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print(f"Test 5 passed: {nums5} -> {result5}")

    # Test case 6: Larger numbers
    nums6 = [10, 20, 30, 39]
    expected6 = 2  # (10,30,40), (20,30,40)
    result6 = triangle_number(nums6)
    assert result6 == expected6, f"Test 6 failed: expected {expected6}, got {result6}"
    print(f"Test 6 passed: {nums6} -> {result6}")

    print("\nAll tests passed!")


if __name__ == "__main__":
    test_triangle_number()