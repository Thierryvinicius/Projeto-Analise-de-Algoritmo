class Heapsort:
    def __init__(self, arr):
        self.arr = arr
        self.heapSort()

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heapsort(self):
        n = len(self.arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(self.arr, n, i)

        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(self.arr, i, 0)