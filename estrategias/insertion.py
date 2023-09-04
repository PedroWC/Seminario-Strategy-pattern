
class Insertion:

    def sort(self, arr: list[int]):
        # Obtém o tamanho da lista
        n = len(arr)
        for i in range(1, n):
            # Armazena o elemento atual que será inserido na posição correta
            key = arr[i]
            # Inicializa o índice para comparar com os elementos à esquerda do 'key'
            j = i - 1

            # Realiza a inserção do elemento 'key' na posição correta à esquerda do 'j'
            while j >= 0 and key < arr[j]:
                # Move o elemento maior para a direita
                arr[j + 1] = arr[j]
                # Move para a posição anterior à esquerda
                j -= 1
            # Insere o 'key' na posição correta
            arr[j + 1] = key

        return arr