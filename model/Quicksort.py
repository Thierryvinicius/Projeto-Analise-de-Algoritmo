class QuickSort:
    def __init__(self, arr, l, h):
        self.arr = arr
        self.l = l
        self.h = h
        self.quicksort(self.arr, self.l, self.h)

    def quicksort(self, arr, l, h):
        if l < h:
            pi = self.dividir(arr, l, h)
            self.quicksort(arr, l, pi - 1)
            self.quicksort(arr, pi + 1, h)

    def dividir(self, arr, l, h):
        # Sua função dividir aqui
        pivot = arr[h]
        i = l - 1
        for j in range(l, h):
            if arr[j] <= pivot:
                i = i + 1
                (arr[i], arr[j]) = (arr[j], arr[i])
        (arr[i + 1], arr[h]) = (arr[h], arr[i + 1])
        return i + 1
