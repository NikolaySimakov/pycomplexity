import shutil
from typing import List, Tuple
from .enums import NotationFormat

'''
Class that contains and represents analysis data
'''
class AnalysisFormatter:
    
    def __init__(
        self, 
        notation_format: NotationFormat, 
        func_name: str = 'No name', 
        func_attrs: List[Tuple[str, str]] | None = None, 
        complexity: str = '1', 
        memory: str = '1',
    ) -> None:
        
        self.notation_format = notation_format
        self.func_name = func_name
        self.func_attrs = func_attrs
        self.complexity = complexity
        self.memory = memory
    
    def report(self, full=True):
        
        print()
        
        if full:
            print('Function name:', self.func_name)
            
            if self.func_attrs:
                print('Function attributes:', ', '.join([f'{attr_name}: {attr_type}' for attr_name, attr_type in self.func_attrs]))
            
            terminal_width = shutil.get_terminal_size().columns
            indent = max((terminal_width - len(self.notation_format.__str__()) - 2)//2, 0)
            print('-' * indent + f' {self.notation_format.__str__()} ' + '-' * indent)
        
        if self.notation_format == NotationFormat.BIG_O:
            print('Сomplexity of algorithm: O({})'.format(self.complexity))
            print('Memory of algorithm: O({})'.format(self.memory))
        
        if self.notation_format == NotationFormat.BIG_OMEGA:
            print('Сomplexity of algorithm: Ω({})'.format(self.complexity))
            print('Memory of algorithm: Ω({})'.format(self.memory))
            
        if self.notation_format == NotationFormat.BIG_THETA:
            print('Сomplexity of algorithm: Θ({})'.format(self.complexity))
            print('Memory of algorithm: Θ({})'.format(self.memory))
        
        print()
        