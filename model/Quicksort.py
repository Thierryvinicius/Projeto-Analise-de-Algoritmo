class QuickSort:
    def __init__(self, dictionary):
        self.dictionary = dictionary

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
    
    def sort_dictionary(self):
        # Converte o dicionário em uma lista de tuplas (chave, valor)
        items = list(self.dictionary.items())

        # Realiza o ordenamento com o Mergesort
        self.quicksort(items, 0, len(items) - 1)

        # Cria um novo dicionário ordenado com base nas tuplas ordenadas
        sorted_dict = {item[0]: item[1] for item in items}
        return sorted_dict
