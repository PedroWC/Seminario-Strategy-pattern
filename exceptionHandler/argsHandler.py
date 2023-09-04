
class ArgsHandler:

    def __init__(self, args):
        if (len(args) > 5):
            print(len(args))
            raise ValueError("Muitos argumentos fornecidos.\nUso: python script.py inc fim stp rpt")
        elif (len(args) < 5):
            raise ValueError("Poucos argumentos fornecidos.\nUso: python script.py inc fim stp rpt")