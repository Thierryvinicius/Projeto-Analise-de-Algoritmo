class Mergesort:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def merge(self, items, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = items[l:m + 1]
        R = items[m + 1:r + 1]

        i = j = 0
        k = l

        while i < n1 and j < n2:
            if L[i][1] <= R[j][1]:
                items[k] = L[i]
                i += 1
            else:
                items[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            items[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            items[k] = R[j]
            j += 1
            k += 1

    def mergesort(self, items, l, r):
        if l < r:
            m = (l + r) // 2
            self.mergesort(items, l, m)
            self.mergesort(items, m + 1, r)
            self.merge(items, l, m, r)

    def sort_dictionary(self):
        # Converte o dicionário em uma lista de tuplas (chave, valor)
        items = list(self.dictionary.items())

        # Realiza o ordenamento com o Mergesort
        self.mergesort(items, 0, len(items) - 1)

        # Cria um novo dicionário ordenado com base nas tuplas ordenadas
        sorted_dict = {item[0]: item[1] for item in items}
        return sorted_dict
