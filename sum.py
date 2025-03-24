def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  
    total = 0  # Initializes a variable to store the sum
    for num in nums:  # Loops through each number in the list
        total += num  # Adds the number to the running total
    return total  # Returns the final total

# Test the function
print("sum_nums returned", sum_nums([1, 2, 3, 4]))
