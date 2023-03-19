def build_heap(data):
    swaps = []
    size = len(data)

    def change(i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] < data[min_index]:
            min_index = left

        if right < n and data[right] < data[min_index]:
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


def main():
  source = input("Enter I for input, F for file...")

    if source == "I":
        size = int(input("Enter size of array..."))
        data = list(map(int, input("Enter elements of array...").split()))
    elif source == "F":
        file_name = input("Enter file name...")
        if "a" not in file_name:
            with open(file_name, "r") as f:
                size = int(f.readline())
                data = list(map(int, f.readline().split()))
        else:
            size = int(file_name[1:])
            data = list(range(1, size + 1))
            data.reverse()

    swaps = build_heap(data)
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

if __name__ == "__main__":
    main()
