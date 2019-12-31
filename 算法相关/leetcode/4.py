def findMedianSortedArrays(nums1, nums2):

    m = len(nums1)
    n = len(nums2)
    r = []
    """
    l1, l2 = 0, 0
    for i in range(m+n):
        if l2 >= n or l1 >= m:
            break
        if nums1[l1] > nums2[l2]:
            r.append(nums2[l2])
            l2 = l2 + 1
        else:
            r.append(nums1[l1])
            l1 = l1 + 1
    if l1 < len(nums1):
        r = r + nums1[l1:]
    elif l2 < len(nums2):
        r = r + nums2[l2:]
    print(r)
    middle = 0
    if (m+n)%2 == 0:
        middle = (r[len(r)//2] + r[len(r)//2 -1])/2
    else:
        middle = r[len(r)//2]
    return middle
    """

    if m == 1 and (m+n) % 2 == 1:

        result = nums2[0]
    if n == 1 and (m + n) % 2 == 1:
        pass
    m1 = findMiddle(nums1)
    m2 = findMiddle(nums2)
    if m1 > m2:
        findMedianSortedArrays(nums1[:len(nums1) // 2 + 1], nums2[len(nums2)//2:])
    else:
        findMedianSortedArrays(nums1[len(nums1) // 2:], nums2[:len(nums2) // 2 + 1])

def findMiddle(nums):
    if len(nums) % 2 == 0:
        middle = (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
    else:
        middle = nums[len(nums) // 2]
    return middle


print(findMedianSortedArrays([1,2,3], [1,2,2]))

