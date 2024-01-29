nums = [1, 2, 3, 4]

n = len(nums)
track = [{"forward": 1, "backward": 1} for _ in range(n)]
finalArr = []
# forward iterate
for i in range(n):
    if i > 0:
        track[i]["forward"] = track[i - 1]["forward"] * nums[i - 1]
# backward iterate
for j in range(n - 1, -1, -1):
    if j < n - 1:
        track[j]["backward"] = track[j + 1]["backward"] * nums[j + 1]
    finalArr.insert(0, track[j]["backward"] * track[j]["forward"])
return finalArr
