def find_ms(xs):
    start_value = 0
    for index, value in enumerate(xs[:]):
        if xs[index]<xs[start_value]:
            start_value = index
    return(start_value)

def selection_sort(xs):
    for i in range(len(xs)):
        temp_index = find_ms(xs[i:])+i
        temp_value = xs[temp_index]
        xs[temp_index], xs[i]= xs[i],temp_value
    return(xs)

xs = [-4,2,5,8,-7,3,6,-1,7]
print(xs)
xs  = selection_sort(xs)
print(xs)
