#Linear search
#We need to loop in the array for the search item
# for index in range(len(data)):
#     if data[index] == search_item:
#         found_index = index
#         found = True
# #Printing output if found item or not        
# if found == True:
#     print(f"Found search item: {search_item} at index: {found_index}")
# else:
#     print(f"{search_item} not found")

#Binary Search
#We need a sorted array of data for searching
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#We need the item to search
#We will need to typecast our input
search_item = int(input("Please enter number to search: "))
#Variable to check if we have found the item
found = False
lower_bound = 0
upper_bound = len(data) - 1

while (lower_bound <= upper_bound):
    index = lower_bound + (upper_bound - lower_bound)//2
    
    if data[index] == search_item:
        found = True
        break
    elif data[index] < search_item:
        lower_bound = index + 1
    else:
        upper_bound = index - 1

if found == True:
    print(f"Item found at index: {index}")
else:
    print(f"Item not found")