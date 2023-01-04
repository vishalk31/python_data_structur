def linear_search(data,target):
    value = -1
    for index in range(len(data)):
        if data[index] == target:
            value = index+1
            
    return (value)

data = [4,5,6,8,9,10,1]
target = 11
result = linear_search(data,target)
if result==-1:
    print("not found")
else:
    print("found and index is : ", result)
