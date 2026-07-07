class Solution:
	def threeSumClosest(self, nums: list[int], target:int) -> list[int]:
		nums.sort()
		n = len(nums)
		
		# Initialize closest sum to infinity
		closest_sum = float('inf')

		for i in range(n):
			# Two pointers
			left = i + 1
			right = n - 1
		
			while left < right:

				# Calculate current sum:
				current_sum = nums[i] + nums[left] + nums[right]
				
				# if we found it return
				if current_sum == target:
					yield [nums[i], nums[left], nums[right]]

				# Update closest sum if current sum is closer to target:
				if abs(current_sum - target) < abs(closest_sum - target):
					closest_sum = current_sum

				# Move pointers based on comparison
				if current_sum > target:
					# Sum is too large, move right pointer left to decrease sum
					right -= 1
				else:
					# Sum is too small, move left pointer right to increase sum
					left += 1

if __name__ == "__main__":
	nums = [-1, 0, 1, 2, -1, -4]
	target = 0
	result = list(Solution().threeSumClosest(nums, target))
	print(result)
	unique_data = [list(x) for x in {tuple(sorted(item)) for item in result}]
	print(unique_data)