
class Heap:

    def sort(self, arr: list[int]):
        # Transforma a lista 'arr' em um heap (árvore binária onde cada nó pai é maior que seus filhos)
        self.heapify(arr)
        
        # Lista que conterá o array ordenado final
        sorted_arr = []
        
        # Enquanto ainda houver elementos no heap (árvore binária), remova o menor elemento (raiz)
        while arr:
            # Remove o menor elemento do heap e adiciona ao array ordenado
            sorted_arr.append(self.heappop(arr))
        
        return sorted_arr

    # Lógica para transformar uma lista em um heap
    def heapify(self, arr: list[int]):
        n = len(arr)
        # Começa a partir do último nó pai e move para baixo para ajustar os elementos
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(arr, n, i)

    # Remove o menor elemento
    def heappop(self, arr: list[int]):
        n = len(arr)
        # Troca o elemento raiz (o menor elemento) com o último elemento
        arr[0], arr[n - 1] = arr[n - 1], arr[0]
        # Remove o último elemento, que agora é o menor
        popped = arr.pop()
        # Reorganiza a árvore heap a partir da raiz para manter a propriedade do heap mínimo
        self.heapify_down(arr, n - 1, 0)

        return popped

    # Ajusta a estrutura do heap conforme necessário para manter as propriedades do heap
    def heapify_down(self, arr: list[int], n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Verifica se o filho esquerdo existe e é menor que o pai
        if left < n and arr[left] < arr[smallest]:
            smallest = left

        # Verifica se o filho direito existe e é menor que o pai ou o filho esquerdo
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        # Se o menor valor não for o pai, faz a troca e chama a função recursivamente
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify_down(arr, n, smallest)
