# sample data

input1 = [2, 3, 6, 8]
inputValue1 = 5

input2 = [4, 8, 15, 23, 42]
inputValue2 = 16

# determine length of input list


def new_list(input_list, input_value):

    length = 0

    for item in input_list:
        length += 1
    # print('length', length)


# find middle position of array

    middle = 0  
    if length % 2 == 0:
        middle = length / 2
        # print('middle even', middle)   
    else:
        middle = (length // 2) + 1
        # print('middle odd', middle)


# for loop through each index and copy value into new list

    output_list = []
    counter = 0
    for index in input_list:
        
        # print('counter %d' % counter)
        # print('index %d' % index)
        if counter < middle:
            output_list += [index]
            counter += 1
        elif counter == middle:
            output_list += [input_value]
            output_list += [index]
            counter += 1
        else:
            output_list += [index]
            counter += 1

    print(output_list)
    return output_list

# sample test cases  #run > python3 shift-array.py in terminal


new_list(input1, inputValue1)
new_list(input2, inputValue2)



