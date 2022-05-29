nums=[7, 4, 5, 7, 3, 2, 8, 6, 8, 7, 6, 5, 11, 9, 7, 3, 8, 7, 6, 5 ]
Sum,Len,Min,Max = sum(nums),len(nums),min(nums),max(nums)
nums.sort()
def medium(num):
    if len(num) % 2 == 0:
        return (num[int(len(num)/2)] + num[int(len(num)/2)])  / 2
    elif len(num) % 2 == 1:
        return num[int(len(num)/2)]
def quartile(num):
    return {"IQ1":num[int(len(num)/4)],
            "IQ3": num[int(len(num)/4*3)],
            "Range":num[int(len(num)/4*3)]-num[int(len(num)/4)]}
def average(num):
    return sum(num)/len(num)
print(medium(nums))
print(quartile(nums))
