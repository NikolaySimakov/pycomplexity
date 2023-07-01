import ast
from pprint import pprint


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
