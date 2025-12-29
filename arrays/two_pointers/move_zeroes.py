"""
Move Zeroes

Problem:
Given an integer array nums, write a function to rearrange the array by moving all zeros
to the end while keeping the order of non-zero elements unchanged. Perform this operation
in-place without creating a copy of the array.

Example:
Input: nums = [2,0,4,0,9]
Output: [2,4,9,0,0]

Constraints:
- Must be done in-place (modify the original array)
- Preserve the relative order of non-zero elements
"""


def move_zeroes(nums):
    """
    Moves all zeros to the end of the array while maintaining the order of non-zero elements.

    Args:
        nums: List[int] - The input array to modify in-place

    Returns:
        None - The function modifies the array in-place
    """
    next_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[next_non_zero], nums[i] = nums[i], nums[next_non_zero]
            next_non_zero += 1
    return nums

def test_move_zeroes():
    """Test cases for the move_zeroes function"""

    # Test case 1: Basic example
    nums1 = [2, 0, 4, 0, 9]
    move_zeroes(nums1)
    assert nums1 == [2, 4, 9, 0, 0], f"Test 1 failed: expected [2, 4, 9, 0, 0], got {nums1}"
    print("✓ Test 1 passed: [2, 0, 4, 0, 9] -> [2, 4, 9, 0, 0]")

    # Test case 2: All zeros
    nums2 = [0, 0, 0]
    move_zeroes(nums2)
    assert nums2 == [0, 0, 0], f"Test 2 failed: expected [0, 0, 0], got {nums2}"
    print("✓ Test 2 passed: [0, 0, 0] -> [0, 0, 0]")

    # Test case 3: No zeros
    nums3 = [1, 2, 3, 4, 5]
    move_zeroes(nums3)
    assert nums3 == [1, 2, 3, 4, 5], f"Test 3 failed: expected [1, 2, 3, 4, 5], got {nums3}"
    print("✓ Test 3 passed: [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]")

    # Test case 4: Single element (zero)
    nums4 = [0]
    move_zeroes(nums4)
    assert nums4 == [0], f"Test 4 failed: expected [0], got {nums4}"
    print("✓ Test 4 passed: [0] -> [0]")

    # Test case 5: Single element (non-zero)
    nums5 = [1]
    move_zeroes(nums5)
    assert nums5 == [1], f"Test 5 failed: expected [1], got {nums5}"
    print("✓ Test 5 passed: [1] -> [1]")

    # Test case 6: Zeros at the beginning
    nums6 = [0, 0, 1, 2, 3]
    move_zeroes(nums6)
    assert nums6 == [1, 2, 3, 0, 0], f"Test 6 failed: expected [1, 2, 3, 0, 0], got {nums6}"
    print("✓ Test 6 passed: [0, 0, 1, 2, 3] -> [1, 2, 3, 0, 0]")

    # Test case 7: Zeros at the end (already sorted)
    nums7 = [1, 2, 3, 0, 0]
    move_zeroes(nums7)
    assert nums7 == [1, 2, 3, 0, 0], f"Test 7 failed: expected [1, 2, 3, 0, 0], got {nums7}"
    print("✓ Test 7 passed: [1, 2, 3, 0, 0] -> [1, 2, 3, 0, 0]")

    # Test case 8: Alternating zeros and non-zeros
    nums8 = [0, 1, 0, 3, 12]
    move_zeroes(nums8)
    assert nums8 == [1, 3, 12, 0, 0], f"Test 8 failed: expected [1, 3, 12, 0, 0], got {nums8}"
    print("✓ Test 8 passed: [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]")

    print("\n✓ All tests passed!")


if __name__ == "__main__":
    test_move_zeroes()