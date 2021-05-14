#1 countdown list
def  countDown(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)
    return newList
print(countDown(5))

#2 print_and_return
def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([1,2]))

#3 first_plus_length
def first_plus_length(list):
    print(list[0])
    return len(list)
print(first_plus_length([1,2,3,4,5]))

#4 values_greater_than_second
def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = [] #greaterThan = list[1]
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([1,2]))
print(values_greater_than_second([1]))
print(values_greater_than_second([]))
#5 length_and_value
def length_and_value(size,value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(length_and_value(4,7))
print(length_and_value(6,2))