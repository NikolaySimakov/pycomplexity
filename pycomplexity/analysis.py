import ast
import shutil
from typing import List, Tuple
from pprint import pprint
from enum import Enum


'''
AST analyzer
'''
class Analyzer(ast.NodeVisitor):
    def __init__(self) -> None:
        self.stats = {
            'for': 0,
            'import': [],
        }
    
    def visit_For(self, node):
        for alias in node.names:
            self.stats['for'].append(alias.name)
        self.generic_visit(node)
    
    def visit_Import(self, node):
        for alias in node.names:
            self.stats["import"].append(alias.name)
        self.generic_visit(node)
    
    def report(self):
        pprint(self.stats)


'''
Notation format enum
'''
class NotationFormat(Enum):
    
    BIG_O : str = 'BIG O'
    BIG_OMEGA : str = 'BIG Ω (OMEGA)'
    BIG_THETA : str = 'BIG Θ (THETA)'
    
    def __str__(self) -> str:
        return str(self.value)


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
        