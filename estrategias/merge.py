
class Merge:

    def sort(self, arr: list[int]):
        # Verifica se a lista contém mais de um elemento
        if len(arr) > 1:
            # Encontra o índice do meio da lista
            mid = len(arr) // 2
            # Divide a lista em duas metades: a esquerda e a direita
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Chama recursivamente o sort nas duas metades da lista
            self.sort(left_half)
            self.sort(right_half)

            # Índices para percorrer as sublistas
            i = j = k = 0

            # Combina as sublistas ordenadas em uma única lista ordenada
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    # Coloca o elemento da esquerda na lista final
                    arr[k] = left_half[i]
                    i += 1
                else:
                    # Coloca o elemento da direita na lista final
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            # Adiciona os elementos restantes da sublista esquerda
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            # Adiciona os elementos restantes da sublista direita
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        return arr