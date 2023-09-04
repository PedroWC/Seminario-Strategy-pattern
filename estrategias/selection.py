

class Selection:

    def sort(self, arr: list[int]):
        # Obtém o tamanho da lista
        n = len(arr)
        for i in range(n):
            # Inicializa o índice do elemento mínimo como 'i'
            min_idx = i
            # Loop para encontrar o índice do elemento mínimo restante
            for j in range(i + 1, n):
                # Verifica se o elemento atual é menor que o elemento mínimo atual
                if arr[j] < arr[min_idx]:
                    # Atualiza o índice do elemento mínimo
                    min_idx = j
            # Troca o elemento na posição 'i' com o elemento mínimo encontrado
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr