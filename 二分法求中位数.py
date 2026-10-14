nums1 = [1,2];nums2 = [3,4]
n=len(nums1)
m=len(nums2)
half = (n + m + 1 )//2
left , right = 0 , n
while left <= right:
    i = (left + right)//2
    j = half - i
    A_left = nums1[i-1] if i > 0 else float('-inf')
    A_right = nums1[i] if i < n else float('inf')
    B_left = nums2[j-1] if j > 0 else float('-inf')
    B_right = nums2[j] if j < m else float('inf')
    if A_left <= B_right and B_left <= A_right:
        if (n + m) % 2 == 1:
            print( max(A_left,B_left))
        print( (max(A_left , B_left)+min(A_right , B_right))/2)
    elif A_left > B_right:
        right = i -1
    else:
        left = i + 1