def build_heap(data):
    swaps = []
    n = len(data)

    def shift_down(i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] < data[min_index]:
            min_index = left

        if right < n and data[right] < data[min_index]:
            min_index = right

        if i != min_index:
            swaps.append((i, min_index))
            
            data[i], data[min_index] = data[min_index], data[i]
            shift_down(min_index)

    for i in range(n // 2, -1, -1):
        shift_down(i)

    return swaps


def main():
    data = []
    text = input("Enter I for input, F for file...")

    if "I" in text:
        n = int(input("Enter size of array..."))
        data = list(map(int, input("Enter elements of array...").split()))

    elif "F" in text:
         file_name = input("Enter file name: ")
        if "a" not in file_name:
            path = './tests/' + file_name
            with open(path, 'r', encoding='utf-8') as file:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))

    swaps = build_heap(data)

    print("Array is converted into a heap in", len(swaps), "swaps")
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
