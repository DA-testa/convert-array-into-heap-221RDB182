    def shift_down(i):
        nonlocal swaps
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
            
    def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        shift_down(i)

    return swaps

def main():
    while True:
        text = input("Enter I for input, F for file...")

        if "I" in text:
            n = int(input("Enter size of array..."))
            data = list(map(int, input("Enter elements of array...").split()))
            break

        if "F" in text:
            file_name = input("Enter file name...")
            with open(file_name, "r") as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
            break

    swaps = build_heap(data)
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

if __name__ == "__main__":
    main()
