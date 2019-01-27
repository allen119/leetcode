# better answer from @老表
# https://blog.csdn.net/qq_39241986/article/details/82799897 
# 这个题目看似很简单，在一个列表(nums)里面找到两数,满足和为事先指定好的数(target),其实有陷阱.
# 第一：很多人一看到题目自然想到两层for循环解决问题，but这种人人都想到的问题你若是也这么做，
# 如#果你就这种程度，面试失败也不算亏；
# 第二：这题的返回值到底是什么？你看清了吗？它的返回值是一个列表，列表里是int型的数据，
# 这个数据并不是我们找到的满足算式的数，而是这个数在列表里对应的下标,你中招了吗？
# 第三：双for循环极易出错的地方，不能出现自己加自己的情况。
 

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        l = len(nums)
        for a in range(l):
            one_num = nums[a]
            other_one = target - one_unm
            if other_one in nums:
	            b = nums.index(other_one)
	            if a != b:
		            if a>b:
		                return [b,a]
		            return [a,b]



# the best one 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        dict_nums = {nums[i]:i for i in range(l)}
        for a in range(l):
            one_unm = nums[a]
            other_one = target - one_unm
            if other_one in dict_nums and a!= dict_nums[other_one]:
                return [a,dict_nums[other_one]]
！