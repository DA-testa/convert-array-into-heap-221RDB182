def build_heap(data):
    swaps = []
    size = len(data)

    def change(i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < size and data[left] < data[min_index]:
            min_index = left
            
        if right < size and data[right] < data[min_index]:
            min_index = right
            
        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]
            swaps.append((i, min_index))
            shift_down(min_index)
            
    def shift_down(i):
        change(i)

    for i in range(size // 2, -1, -1):
        shift_down(i)

    return swaps


def main(): # input from keyboard
    text = input("Enter 'I' (input) or 'F' (file)")
    if "F" in text:
        file_name = input("file name: ")
        path = './tests/' + file_name
        with open(path, 'r', encoding='utf-8') as file:
            size = int(file.readline())
            data = list(map(int, file.readline().split()))
    elif "I" in text:
        size = int(input())
        data = list(map(int, input().split()))
                                         
    assert data is not None and len(data) == size   # checks if lenght of data is the same as the said lenght
    swaps = build_heap(data)                        # calls function to assess the data and give back all swaps
    assert len(swaps) <= size*4                     # this number should be less than 4n (less than 4*len(data))

    print(len(swaps))   # output all swaps
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
