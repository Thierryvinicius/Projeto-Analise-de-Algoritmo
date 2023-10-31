class buscaBinaria:

    def __init__(self):

        def pesquisa_binaria_recursiva(A, esquerda, direita, item):
            """Implementa pesquisa binária recursivamente."""
            # 1. Caso base: o elemento não está presente. 
            if direita < esquerda:
                return -1
            meio = (esquerda + direita) // 2
            # 2. Nosso palpite estava certo: o elemento está no meio do arranjo. 
            if A[meio] == item:
                return meio
            # 3. O palpite estava errado: atualizamos os limites e continuamos a busca. 
            elif A[meio] > item:
                return pesquisa_binaria_recursiva(A, esquerda, meio - 1, item)
            else: # A[meio] < item
                return pesquisa_binaria_recursiva(A, meio + 1, direita, item)