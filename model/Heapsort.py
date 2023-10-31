class Heapsort:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def heapify(self, items, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and items[i][1] < items[l][1]:
            largest = l

        if r < n and items[largest][1] < items[r][1]:
            largest = r

        if largest != i:
            items[i], items[largest] = items[largest], items[i]
            self.heapify(items, n, largest)

    def heapsort(self):
        items = list(self.dictionary.items())
        n = len(items)

        # Constrói a max-heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(items, n, i)

        # Extrai elementos da heap, um por um
        for i in range(n - 1, 0, -1):
            items[i], items[0] = items[0], items[i]  # Troca o elemento máximo (raiz da heap) com o último
            self.heapify(items, i, 0)  # Chama heapify na heap reduzida

        sorted_dict = {item[0]: item[1] for item in items}
        return sorted_dict
