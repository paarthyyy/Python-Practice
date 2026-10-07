def missingNumber(self, nums: list[int]) -> int:
    n=len(nums)
    a= n * (n + 1) // 2
    return  a - sum(nums)
