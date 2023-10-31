class QuickSort:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def quicksort(self, items, l, h):
        if l < h:
            pi = self.dividir(items, l, h)
            self.quicksort(items, l, pi - 1)
            self.quicksort(items, pi + 1, h)

    def dividir(self, items, l, h):
        pivot = items[h]
        i = l - 1
        for j in range(l, h):
            if items[j][0] <= pivot[0]:
                i = i + 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[h] = items[h], items[i + 1]
        return i + 1

    def sort_dictionary(self):
        # Converte o dicionário em uma lista de tuplas (chave, valor)
        items = list(self.dictionary.items())

        # Realiza o ordenamento com o QuickSort
        self.quicksort(items, 0, len(items) - 1)

        # Cria um novo dicionário ordenado com base nas tuplas ordenadas
        sorted_dict = {item[0]: item[1] for item in items}
        return sorted_dict
