import numpy as np 

def major_element(num_list):
    result_dict = {}

    for num in num_list:
        if num in result_dict:
            result_dict[num] += 1
        else:
            result_dict[num] = 1
    
    for key, val in result_dict.items():
        if val > len(num_list) / 2:
            return key
    
    return -1


def major_element_2(num_list):
    if len(num_list) == 0:
        return -1
    
    num_set = set(num_list)
    for el in num_set:
        if num_list.count(el) > 0.5*len(num_list):
            return el

    return -1



if __name__ == '__main__':
    nums = [1, 2, 3, 4, 4, 5, 4]
    re = major_element_2(nums)
    print(re)

