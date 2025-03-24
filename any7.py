def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    for num in nums:  # Loops through the list of numbers
        if num == 7:  # Checks if the current number is 7
            return True  # Returns True immediately if a 7 is found
    return False  # If the loop finishes without finding a 7, returns False

# Test cases
print("should be true:", any7([1, 2, 7, 4, 5]))  # Output: should be true: True
print("should be false:", any7([1, 2, 4, 5]))    # Output: should be false: False
