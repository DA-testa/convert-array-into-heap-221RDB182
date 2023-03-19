def build_heap(data):
    swaps = []
    n = len(data)
    
    for i in range(n//2, -1, -1):
        shift_down(i)

    def shift_down(i):
        nonlocal swaps
        min_index = i
        left = 2*i+1
        right = 2*i+2

        if left < n and data[left] < data[min_index]:
            min_index = left

        if right < n and data[right] < data[min_index]:
            min_index = right

        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            shift_down(min_index)
    return swaps


def main():
    # input from keyboard
    text = input("Enter I for input, F for file...")
    if "F" in text:
        file_name = input("Enter file name: ")
        if "a" not in file_name:
            path = './tests/' + file_name
            with open(path, 'r', encoding='utf-8') as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
    
        
    elif "I" in text:
        n = int(input("Enter size of array..."))
        data = list(map(int, input("Enter elements of array...").split()))
    else:
        print("Error. Please enter 'I' or 'F'.")
 
    # checks if lenght of data is the same as the said lenght
    assert data is not None and len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)
    
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= n*4

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
