import sys

def largest_series_product(nums):
    # Create max multiple first 13, iterate then next 13
    max = 0
    for i in range(len(nums)-13):
        cur = 1
        for j in range(i, i+13):
            cur *= int(nums[j])
        if max < cur:
            max = cur
            
    return max
    

def read_file_bytes():
    nums = []
    with open("num", "rb") as f:
        byte = f.read(1)
        while byte != "":
            nums.append(byte)
            byte = f.read(1)
    
    return nums

        
if __name__ == "__main__":
    print largest_series_product(read_file_bytes())