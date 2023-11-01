class BuscaBinaria:

    def busca_binaria(self, dicionario, indice_alvo):
        chaves_ordenadas = sorted(dicionario.keys())

        esquerda, direita = 0, len(chaves_ordenadas) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            chave_meio = chaves_ordenadas[meio]
            print('CHAVES ORDENADAS: ', chaves_ordenadas[meio])
            print('CHAVE MEIO: ',chave_meio)
            print('ALVO: ', indice_alvo)

            if chave_meio == indice_alvo:
                return chave_meio  # Retorna a chave correspondente ao valor alvo
            elif chave_meio < indice_alvo:
                esquerda = meio + 1
            else:
                direita = meio - 1
        return None
