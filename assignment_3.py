def sort_number(arr):
    oddArr = []
    evenArr = []
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            evenArr.append(arr[i])
        else:
            oddArr.append(arr[i])

    oddArr = sort(oddArr)
    evenArr = sort(evenArr)

    return evenArr + oddArr

def sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr