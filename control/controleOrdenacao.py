# control/controleOrdenacao.py

from model import Mergesort,Heapsort,Quicksort

def process_sorting(method, input_data):
    if method == "Mergesort":

        mergesort_instance = Mergesort.Mergesort(input_data)
        sorted_dict = mergesort_instance.sort_dictionary()
        print(sorted_dict)
        return sorted_dict

    if method == "Heapsort":

        heapsort_instance = Heapsort.Heapsort(input_data)
        sorted_dict = heapsort_instance.heapsort()
        print(sorted_dict)
        return sorted_dict

    if method == "Quicksort":

        quicksort_instance = Quicksort.QuickSort(input_data)
        sorted_dict = quicksort_instance.sort_dictionary()
        print(sorted_dict)
        return sorted_dict