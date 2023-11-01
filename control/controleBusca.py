from model import busca_binaria

def processing_search(data,key):
    search_instance = busca_binaria.BuscaBinaria()
    search = search_instance.busca_binaria(data,key)
    return search
