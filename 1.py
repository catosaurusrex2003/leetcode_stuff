def min_operations(nums, K):
    if(K == len(nums)):
        return 1
    max_num = max(nums)
    # maxindex = nums.index(max_num)
    myCount = nums.count(max_num) -1
    size=len(nums) - myCount
    # if size
    if(size%2==0):
        return size//(K-1)
    else:
        return size//(K-1)

N = int(input())
nums = list(map(int, input().split()))
K = int(input())

# result = min_operations(nums, K)
# print(result)

print(6//4)
