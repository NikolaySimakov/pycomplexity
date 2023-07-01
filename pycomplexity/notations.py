import ast
import inspect
from typing import List, Tuple

from pycomplexity.analysis import Analyzer, AnalysisFormatter, NotationFormat


'''
Base class of asymptotic notation
'''
class AsymptoticNotation:

    def __init__(self, full_report: bool = True) -> None:
        self.full_report = full_report
    
    def _code_to_string(self, func) -> str:
        code = inspect.getsource(func)
        code_lines = code.split('\n')[1:]
        modified_code = '\n'.join(code_lines)
        return modified_code
    
    def _get_ast(self, func) -> ast.Module:
        code_str = self._code_to_string(func)
        return ast.parse(code_str)
    
    def analyze(self, func):
        analyzer = Analyzer()
        tree = self._get_ast(func)
        # print(ast.dump(tree, indent=4))
        
        for node in ast.walk(tree):
            # print(node)
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
            
            if isinstance(node, ast.For):
                print(node, node.body, node.iter)

        # analyzer.visit(tree)
        # analyzer.report()
        
        return func_name or 'No name', ...
    
    def report(func):
        def wrapper(self, *args, **kwargs):
            analysis_formatter: AnalysisFormatter = func(self, *args, **kwargs)
            return analysis_formatter.report(full=self.full_report)
        return wrapper


'''
Implementation of Big O notation
'''
class BigO(AsymptoticNotation):

    def __init__(self) -> None:
        super().__init__()
    
    @AsymptoticNotation.report
    def complexity(self, func) -> AnalysisFormatter:
        
        func_name, _ = self.analyze(func)
        
        return AnalysisFormatter(
            func_name=func_name,
            notation_format=NotationFormat.BIG_O,
        )


'''
Implementation of Big Omega notation
'''
class BigOmega(AsymptoticNotation):
    
    def __init__(self) -> None:
        super().__init__()
    
    @AsymptoticNotation.report
    def complexity(self, func) -> AnalysisFormatter:
        
        func_name, _ = self.analyze(func)
        
        return AnalysisFormatter(
            func_name=func_name,
            notation_format=NotationFormat.BIG_OMEGA,
        )
        
        
'''
Implementation of Big Theta notation
'''
class BigTheta(AsymptoticNotation):
    
    def __init__(self) -> None:
        super().__init__()
    
    @AsymptoticNotation.report
    def complexity(self, func) -> AnalysisFormatter:
        
        func_name, _ = self.analyze(func)
        
        return AnalysisFormatter(
            func_name=func_name,
            notation_format=NotationFormat.BIG_THETA,
        )