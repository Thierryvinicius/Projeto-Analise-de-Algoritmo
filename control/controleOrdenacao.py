# control/controleOrdenacao.py

from model import Mergesort,Heapsort,Quicksort

def process_sorting(method, input_data):
    if method == "Mergesort":
        print('dentro do merge')
        mergesort_instance = Mergesort.Mergesort(input_data)
        sorted_dict = mergesort_instance.sort_dictionary()
        print(sorted_dict)
        return sorted_dict

    if method == "Heapsort":
        sorted_data = Heapsort.Heapsort(input_data)
    if method == "Quicksort":
        print('dentro do quick')
        sorted_data = Quicksort.QuickSort(input_data, 0, len(input_data) - 1)
        print('deu certo!!!')
        print(sorted_data)