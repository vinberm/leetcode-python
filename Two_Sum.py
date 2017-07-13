class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) <= 1:
                return False
        result = {}
        for i in range(len(nums)):
            if nums[i] in result:
                return [result[nums[i]], i]
            else:
                result[target - nums[i]] = i





def main():
    list1 = [1, 2, 4]
    list2 = [1, 4, 5, 12, 87, 23]
    target = [6, 13]
    solu = Solution()

    result1 = solu.twoSum(list1, target[0])
    result2 = solu.twoSum(list2, target[1])
    print("result1: ", result1)
    print("result2: ", result2)


if __name__ == '__main__':
    main()
