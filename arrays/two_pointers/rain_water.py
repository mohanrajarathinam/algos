"""
Rain Water Trapping Problem

Problem Statement:
Given n non-negative integers representing an elevation map where the width of each bar is 1,
calculate how much water can be trapped after raining.

The water trapped at any position is determined by the minimum of:
- The maximum height to the left of that position
- The maximum height to the right of that position
minus the height at that position itself.

Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The elevation map can trap 6 units of water.

Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""


def trap(height: list[int]) -> int:
    """
    Calculate the total amount of water that can be trapped.

    Args:
        height: List of non-negative integers representing bar heights

    Returns:
        Total units of water trapped
    """
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    total_water = 0
    while left < right:
        if left_max < right_max:
            left += 1
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total_water += left_max - height[left]
        else:
            right -= 1
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total_water += right_max - height[right]

    return total_water


def test_trap():
    """Test cases for the trap function."""

    # Test case 1: Standard example
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Test case 1 failed"
    print("✓ Test case 1 passed: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6")

    # Test case 2: Another standard example
    assert trap([4, 2, 0, 3, 2, 5]) == 9, "Test case 2 failed"
    print("✓ Test case 2 passed: [4,2,0,3,2,5] -> 9")

    # Test case 3: No water can be trapped
    assert trap([1, 2, 3, 4, 5]) == 0, "Test case 3 failed"
    print("✓ Test case 3 passed: [1,2,3,4,5] -> 0 (ascending)")

    # Test case 4: Descending heights
    assert trap([5, 4, 3, 2, 1]) == 0, "Test case 4 failed"
    print("✓ Test case 4 passed: [5,4,3,2,1] -> 0 (descending)")

    # Test case 5: Valley shape
    assert trap([3, 0, 2, 0, 4]) == 7, "Test case 5 failed"
    print("✓ Test case 5 passed: [3,0,2,0,4] -> 7")

    # Test case 6: Single element
    assert trap([5]) == 0, "Test case 6 failed"
    print("✓ Test case 6 passed: [5] -> 0 (single element)")

    # Test case 7: Two elements
    assert trap([3, 2]) == 0, "Test case 7 failed"
    print("✓ Test case 7 passed: [3,2] -> 0 (two elements)")

    # Test case 8: All zeros
    assert trap([0, 0, 0, 0]) == 0, "Test case 8 failed"
    print("✓ Test case 8 passed: [0,0,0,0] -> 0 (all zeros)")

    # Test case 9: Multiple peaks
    assert trap([2, 1, 2, 1, 2]) == 2, "Test case 9 failed"
    print("✓ Test case 9 passed: [2,1,2,1,2] -> 2")

    # Test case 10: Large gap
    assert trap([5, 0, 0, 0, 5]) == 15, "Test case 10 failed"
    print("✓ Test case 10 passed: [5,0,0,0,5] -> 15")

    print("\n🎉 All test cases passed!")


if __name__ == "__main__":
    test_trap()