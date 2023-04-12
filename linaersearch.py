



def linear_search(list,target):# function takes two parameters one list as list function and the target.
    """ Return the index position of the target if found , else returns None """
    for i in range(0, len(list)): # this will look from 0 index to the end of the list.
        if list[i] == target: # if the list index equal the target, the if statement will be execute 
            print('number has found') # print
            return i # it will return the index what found in i
        return None # otherwise it will return None

def verfiy(index): # function takes one parameter as index variable
    if index is not None: # checking if index not return None 
        print('Target found in index', index) # print found target and the index variable
    else:
        print('Target Not found in list') # otherwise it will print not founded target

# here you can use two ways for determine your list
# first way:
numbers = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 5) # call the linear func and give it the list and the target number
verfiy(result) # we passing the result as parameter in verfiy func in place of index
# second way: 
newlist = [] # we made an empty list
for i in range(0,10): # here you can decide the range of the list without typing manually
    newlist.append(i) # here we add every index from the range func to our empty list
result = linear_search(newlist, 9) # as the first way we call linear_search func and we passing the newlist and target 
verfiy(result) # finally we passing to verfiy func the variable result.




