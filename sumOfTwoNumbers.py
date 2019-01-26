#leecode training camp.  #47  
#https://leetcode-cn.com/problems/two-sum/.    sum of two numbers
#target - num1 = num2  then find num2 in the rest of nums (binary search)

class Solution(object):
	def twoSum(self, nums, target):
		nums.sort()
		result = []
		n = len(nums)
		for i in nums:
			j = self.BinarySearch( nums, target - i)
			if j != -1:
				result.append(i)
				result.append(j)
				print(result)
				return result
		return "can't find the two numbers"

#Binary Search  O(log2n)
	def BinarySearch(self, array, t):
		low = 0
		height = len(array) - 1
		while low < height:
			mid = (low + height)//2
			if array[mid] < t:
				low = mid + 1
			elif array[mid] > t:
				height = mid - 1
			else:
				return array[mid]
		return -1
		
s = Solution()
nums = [2,8,17,4,5,6,13]
sum = 11
s.twoSum(nums, sum)