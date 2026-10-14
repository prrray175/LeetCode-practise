nums = [-2, 0, 1, 1, 2]
nums.sort()
result = []
for i in range(len(nums) - 2):
    if i!=0 and nums[i] == nums[i - 1]:#防止出现第一个元素重复
        continue
    x = nums[i]
    left, right = i+1, len(nums) - 1
    while left < right:
        y = nums[left]
        z = nums[right]
        if x + y + z == 0 :
            result.append([x,y,z])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left-1]:#找到答案后跳过重复的数据
                left += 1
            while left < right and nums[right] == nums[right+1]:
                right -= 1
        elif x + y + z < 0:#数值偏小说明nums[left]值偏小了
            left += 1
        else:
            right -= 1
print(result)
