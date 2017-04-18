# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases
nums = [15, 2, 3, 4, 3, 6]

def odd_average(nums):
    odds = 0
    odd_num = []
    for num in nums:
        if num%2 == 1:
            odds += num
            odd_num.append(num)
    return odds//len(odd_num)

print(odd_average(nums))
