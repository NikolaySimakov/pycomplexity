import ast
from pprint import pprint
from enum import Enum


'''
AST analyzer
'''
class Analyzer(ast.NodeVisitor):
    def __init__(self) -> None:
        self.stats = {
            'vars' : [],
            'for' : [],
            'import': [],
        }
    
    def visit_vars(self, node):
        for alias in node.names:
            self.stats['vars'].append(alias.name)
        self.generic_visit(node)
    
    def visit_for(self, node):
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
    
    BIG_O : str = 'BIG_O'
    BIG_OMEGA : str = 'BIG_OMEGA'
    
    def __str__(self) -> str:
        return str(self.value)


'''
Class that contains and represents analysis data
'''
class AnalysisFormatter():
    def __init__(self, notation_format: NotationFormat) -> None:
        self.notation_format = notation_format
    
    def __repr__(self) -> str:
        pass
    
    def console_format(self) -> str:
        pass