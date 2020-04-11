some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

#Do Type Casting of the set on the list to remove the duplicate values
new_set = set(some_list)

#Duplicates are removed
print(f'The New set is:{new_set}')

#Make the newset to list using list type casting.
new_list = list(new_set)

#print the newlist.
print('The New list is:{}'.format(new_list))

#Sort the list
new_list.sort()

#print the newlist
print('The New list is:{}'.format(new_list))


#Make Duplicates into new list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

#creates a new list
duplicates = list()

#loop thru each value in the list
for value in some_list:
    
    #check if count greater than 1 and value should not be present in the duplicates.
    # This is to avoid counting same duplicate value again
    if(some_list.count(value) > 1 and value not in duplicates):
        
        #adding item into list
        duplicates.append(value)
        
#Duplicates are removed
print(f'The Duplicate values are :{duplicates}')
