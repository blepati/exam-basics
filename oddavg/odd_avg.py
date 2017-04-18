# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases
nums = [1, 2, 3, 4, 5]

def odd_average(nums):
    odds = 0
    odd_num = []
    for num in nums:
        try:
            if num%2 == 1:
                odds += num
                odd_num.append(num)
            return odds//len(odd_num)
        except ZeroDivisionError:
            return 0

print(odd_average(nums))
