class SortContext:

    def __init__(self, strategy: function):
        self.strategy = strategy
    
    def execute(self, data: list) -> list:
        return self.strategy.sort(data)