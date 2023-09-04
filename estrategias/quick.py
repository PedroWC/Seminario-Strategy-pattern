
class Quick:

    def sort(self, arr: list[int]):
        # Verifica se o tamanho da lista é menor ou igual a 1, o que significa que está ordenada
        if len(arr) <= 1:
            return arr

        # Escolhe o elemento do meio da lista como pivô para a partição
        pivot = arr[len(arr) // 2]

        # Separa os elementos em três listas: menores que o pivô, iguais ao pivô e maiores que o pivô
        # Elementos menores que o pivô
        left = [x for x in arr if x < pivot]
        # Elementos iguais ao pivô
        middle = [x for x in arr if x == pivot]
        # Elementos maiores que o pivô
        right = [x for x in arr if x > pivot]

        # Chama recursivamente o algoritmo em cada sublista à esquerda e à direita do pivô
        # e concatena as sublistas ordenadas com o pivô no meio
        return self.sort(left) + middle + self.sort(right)