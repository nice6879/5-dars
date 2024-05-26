def notogri_raqam(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return nums[i]
    return None  

nums = [1, 2, 3, 5, 4, 6, 7]
x = notogri_raqam(nums)
print(f"xato joylashgan raqam: {x}")
