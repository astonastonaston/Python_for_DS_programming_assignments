# import itertools as it

# def next_permutation(t):
#     """Compute the amount of water trapped, given the wall height sequence"""
#     assert type(t)==tuple
#     for i in t:
#         assert type(i)==int
#     assert len(tuple(set(t)))==len(t)
#     tL = list(t)
#     tLSo = sorted(tL)
#     allts = list(it.permutations(tLSo))
#     allnts = list(it.permutations(tLSo))
#     allnts.insert(0, allnts[-1])
#     allnts.pop()
#     allDict = dict(zip(allnts, allts))
#     return allDict[t]

# def next_permutation(t):
#     """Compute the amount of water trapped, given the wall height sequence"""
#     assert type(t)==tuple
#     for i in t:
#         assert type(i)==int
#     assert len(tuple(set(t)))==len(t)
#     tL = list(t)
#     tLSo = sorted(tL)
#     allts = it.permutations(tLSo)
#     while (next(allts) != t):
#         continue
#     try:
#         nx = next(allts)
#     except:
#         return tuple(tLSo)
#     return nx

# def findRightMax(index,a,curr):
#     """find max index of the number > the current number, on right sublist"""
#     if (index==len(a)-1):
#         return None
#     else:
#         for i in range(len(a)-1, index, -1):
#             if (a[i] > curr):
#                 return i
#         return None


# def findLeftMax(index,a,curr):
#     """find max index of the number > the current number, on left sublist"""
#     if (index==0):
#         return None
#     else:
#         for i in range(index):
#             if (a[i] > curr):
#                 return i
#         return None




# def findMaxIndex(index,a,curr):
#     """find max index of the number > the current number"""
#     ans = findRightMax(index,a,curr)
#     if (ans != None):
#         return ans
#     else:
#         return findLeftMax(index,a,curr)

# def findMaxIndex(a,curr):
#     """find max index of the number > the current number"""
#     ans = -1
#     index = 0
#     for i in range(index,len(a)):
#         if a[i]>curr:
#             if ans == -1:
#                 ans = curr
#                 index = i
#             else:
#                 ans = min(ans,a[i])
#                 index = i
#     return index


# def findMaxIndex(a,curr):
#     """find max index of the number > the current number"""
#     index = 0
#     for i in range(index,len(a)):
#         if a[i]>curr:
#             index = i
#     return index




def next_permutation(nums):
    """
    get the next permutation in lex order
    """
    assert type(nums)==tuple
    for i in nums:
        assert type(i)==int
    assert len(tuple(set(nums)))==len(nums)
    nums = list(nums)
    found = False
    i = len(nums)-2
    while i >=0:
       if nums[i] < nums[i+1]:
        found =True
        break
       i-=1
    if not found:
       nums.sort()
    else:
      index = 0
      for j in range(index,len(nums)):
          if nums[j]>nums[i]:
              index = j
      nums[i],nums[index] = nums[index],nums[i]
      nums[i+1:] = nums[i+1:][::-1]
    nums = tuple(nums)
    return nums

# def main():
#     t = (0, 5, 2, 1, 4, 7, 3, 6)
#     print(next_permutation(t))
#     t = (2,3,1)
#     print(next_permutation(t))
#     t = (3,2,1,0)
#     print(next_permutation(t))
#     return 0

# main()