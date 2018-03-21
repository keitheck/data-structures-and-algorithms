# sample data

input1 = [2, 3, 6, 8]
inputValue1 = 5

input2 = [4, 8, 15, 23, 42]
inputValue2 = 16

# declarations
# length = 0
# middle = 0


# determine length of input list

# def list_length(input_list):
#     length = 0
#     for item in input_list:
#         length += 1
#     print('length', length)
#     return length


# find middle position of array

def middle_position(length):
    print(length)
    middle = 0  
    if length % 2 == 0:
        middle = length / 2
        print('middle even', middle)
        return middle
    else:
        middle = (length // 2) + 1
        print('middle odd', middle)
        return middle


# for loop through each index and copy value into new list

def new_list(input_list, input_value):

    length = 0

    for item in input_list:
        length += 1
    print('length', length)
    
    middle = 0  
    if length % 2 == 0:
        middle = length / 2
        print('middle even', middle)   
    else:
        middle = (length // 2) + 1
        print('middle odd', middle)
        
    output_list = []
    for index in input_list:
        if index < middle:
            output_list += [index]
        elif index == middle:
            output_list += [input_value]
            output_list += [index]
        else:
            output_list += [index]

    print(output_list)
    return output_list

new_list(input1, inputValue1)



