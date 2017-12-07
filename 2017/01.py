def weird_sum(nums):
    # initialize sum
    s = 0
    # copy first item to the end so we can consider it circular
    nums += nums[0]
    # don't step to the last as we look one further
    for i in range(len(nums) - 1):
        # if the item is the same as next one
        if nums[i] == nums[i+1]:
            # add its value to sum
            s += int(nums[i])
    return s
            
def weird_sum2(nums):
    l = len(nums)       # store length of input
    m = l / 2           # store the offset
    s = 0               # initialize sum
    for i in range(l):
        if nums[i] == nums[(i+m) % l]:
            s += int(nums[i])
    print s

def weird_sum(nums, offset=None):
    # calculate and store length of input
    l = len(nums)
    # offset differs for both parts of the task
    if offset is not None:
        m = offset
    else:
        m = l / 2
    # initialize sum
    s = 0
    for i in range(l):
        # position i is compared to position (i + m) modulo l
        if nums[i] == nums[(i + m) % l]:
            s += int(nums[i])
    print s

with open("01-input", "r") as f:
    inp = f.read().splitlines()[0]

# first part
weird_sum(inp, offset=1)
# second part
weird_sum(inp)
