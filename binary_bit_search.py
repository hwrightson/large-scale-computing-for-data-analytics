def fun_binary_search(my_arr, len_array, val):
    step = 1
    while (step < len_array):
        step <<= 1

    i = 0
    while (step):
        if (i + step < len_array and my_arr[i + step] <= val):
            i += step
        step >>= 1

    if (my_arr[i] == val):
        return i
    

def main():
    my_array = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    len_array = len(my_array)
    val = 11
    print(fun_binary_search(my_array, len_array, val))
    print("Hello World!")

main()
