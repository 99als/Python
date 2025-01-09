def sum_of_squares(nums):
    total = 0
    for num in nums:
        total += (num**2)
    return total

def product(nums):
    total = 1
    for num in nums:
        total *= num
    return total

def sum_sq_prod(nums):
    return sum_of_squares(nums) + product(nums)