#Input [7,9,3,5,6]
#OutPut 3
#Plain English, given a rotated sorted list, 
# rotated a number of times we neeed to find the number of times it was rotated

def find_nums_rotated(nums:list):
    if len(nums)==0:
        return 0
    lo = 0
    hi = len(nums) // 2
    if (nums[len(nums) - 1]> nums[lo]):
        return 0
    while hi >= lo:
        middle = lo + (hi-lo) // 2
        #right
        if middle > nums[0]:
            lo = middle + 1
        if middle < nums[0]:
            hi = middle - 1
        if nums[middle] > nums[middle + 1]:
            return middle + 1
        if nums[middle - 1] > nums[middle]:
            return middle



tests= []
# tests.append({
#     "input":{
#         "nums":[19,25,29,3,5,6,7,9,11,14]
#     },
#     "output":3
# })

# tests.append({
#     "input":{
#         "nums":[4,5,6,7,8,1,2,3]
#     },
#     "output":5
# })

# tests.append({
#     "input":{
#         "nums":[1,2,3,4]
#     },
#     "output":0
# })

# tests.append({
#     "input":{
#         "nums":[]
#     },
#     "output":0
# })

tests.append({
    "input":{
        "nums":[7,3,5]
    },
    "output":1
})

# tests.append({
#     "input":{
#         "nums":[3,5,7,8,9,10]
#     },
#     "output":0
# })



for test in tests:
    result = find_nums_rotated(**test["input"]) == test["output"]
    print(result)