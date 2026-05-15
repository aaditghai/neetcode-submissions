class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct, rightProduct = [], []
        total = 1
        for num in nums:
            total *= num
            leftProduct.append(total)
        total = 1
        for num in nums[::-1]:
            total *= num
            rightProduct.append(total)
        rightProduct = list(reversed(rightProduct))
        res = []
        print(leftProduct)
        print(rightProduct)
        for i in range(len(nums)):
            leftSide = leftProduct[i-1] if i-1 >= 0 else 1
            rightSide = rightProduct[i+1] if i+1 < len(nums) else 1
            print(leftSide, rightSide)
            res.append(leftSide*rightSide)
        return res