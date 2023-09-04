
class Counting:

    def sort(self, arr: list[int]):
        # Verifica se a lista está vazia
        if not arr:
            return arr

        # Encontra o valor máximo na lista e adiciona 1 para definir self, o tamanho da lista de contagem
        max_val = max(arr) + 1
        # Inicializa a lista de contagem com zeros para cada possível valor
        count = [0] * max_val

        # Lista que conterá o array ordenado final
        sorted_arr = []
        
        # Loop para construir o histograma de contagem
        for num in arr:
            # Incrementa a contagem do número atual
            count[num] += 1

        # Constrói o array ordenado baseado nas contagens
        for i, freq in enumerate(count):
            # Adiciona 'i' (valor) 'freq' (contagem) vezes ao array ordenado
            sorted_arr.extend([i] * freq)

        return sorted_arr