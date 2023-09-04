
# Nome: PEDRO HENRIQUE WEBER CARVALHAES

# usado para formatar as tabelas
from prettytable                import PrettyTable
# usado para pegar os parâmetros inc fim stp e rpt
from sys                        import argv
# usado para pegar os tempos de processamento
from time                       import time
# usado para gerar valores pseudo aleatórios
from random                     import randint
# usado para calcular a média dos tempos de processamento
from statistics                 import mean
# usado para calcular quantas valores de n vão dar entre inc e fim
from math                       import ceil
# usado para 
from estrategias.SortContext    import SortContext
from estrategias.counting       import Counting
from estrategias.selection      import Selection 
from estrategias.insertion      import Insertion 
from estrategias.merge          import Merge 
from estrategias.heap           import Heap 
from estrategias.quick          import Quick
# tratamento de exceções
from exceptionHandler.argsHandler import ArgsHandler

class Main:

    def __init__(self, args: list[str]):

        try:
            inc = int(args[1])
            fim = int(args[2])
            stp = int(args[3])
            self.rpt = int(args[4])
        
        except:
            raise ValueError("Argumentos devem ser inteiros.")

        data_types = ["random", "reverse", "sorted", "nearly_sorted"]

        for self.data_type in data_types:
            x = PrettyTable(['n', 'Selection', 'Insertion', 'Merge', 'Heap', 'Quick', 'Counting'])

            [x.add_row(self.run_sorting_algorithms(size)) for size in [i for i in range(inc, fim, stp)]]

            print(f"\n[[{self.data_type.upper()}]]")
            
            print(x)

    def generate_data(self, size) -> list[int]:
        if self.data_type == "random":
            return [randint(0, size*10) for _ in range(size)]
        
        elif self.data_type == "reverse":
            return list(range(size, 0, -1))
        
        elif self.data_type == "sorted":
            return list(range(1, size+1))
        
        elif self.data_type == "nearly_sorted":
            arr = list(range(1, size+1))
            num_swaps = size // 10

            for _ in range(num_swaps):
                i, j = randint(0, size-1), randint(0, size-1)
                arr[i], arr[j] = arr[j], arr[i]

            
            return arr
        
        else: return [0]

    def run_sorting_algorithms(self, size):
        data = self.generate_data(size)
        algorithms = [
            SortContext,
            Counting,
            Selection,
            Insertion,
            Merge,
            Heap,
            Quick
        ]
        results = [f"{size}"]
        for algorithm in algorithms:
            times = []

            for _ in range(self.rpt):

                start_time = time()
                
                sort = SortContext(algorithm)
                sort.execute(data.copy())

                times.append(time() - start_time)
            results.append(f"{mean(times):.6f}")
            
        return results




if __name__ == "__main__":

    ArgsHandler(argv)
     
    Main(argv)