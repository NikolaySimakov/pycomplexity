import ast
import inspect
from typing import List, Tuple

from .analysis import Analyzer
from .formatters import AnalysisFormatter
from .enums import NotationFormat, CommonBigO

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
        
    def constant(self, func) -> CommonBigO:
        is_constant = False
        
        '''
        TODO: function that checks if algorithm has constant complexity
        '''
        
        if is_constant:
            return CommonBigO.CONSTANT
        return CommonBigO.NON_COMMON
    
    def linear(self, func) -> CommonBigO:
        is_linear = False
        
        '''
        TODO: function that checks if algorithm has linear complexity
        '''
        
        if is_linear:
            return CommonBigO.LINEAR
        return CommonBigO.NON_COMMON
    
    def logarithmic(self, func) -> CommonBigO:
        is_logarithmic = False
        
        '''
        TODO: function that checks if algorithm has logarithmic complexity
        '''
        
        if is_logarithmic:
            return CommonBigO.LOGARITHMIC
        return CommonBigO.NON_COMMON
    
    def linearithmic(self, func) -> CommonBigO:
        is_linearithmic = False
        
        '''
        TODO: function that checks if algorithm has linearithmic complexity
        '''
        
        if is_linearithmic:
            return CommonBigO.LINEARITHMIC
        return CommonBigO.NON_COMMON
    
    def quadratic(self, func) -> CommonBigO:
        is_quadratic = False
        
        '''
        TODO: function that checks if algorithm has quadratic complexity
        '''
        
        if is_quadratic:
            return CommonBigO.QUADRATIC
        return CommonBigO.NON_COMMON
    
    def cubic(self, func) -> CommonBigO:
        is_cubic = False
        
        '''
        TODO: function that checks if algorithm has cubic complexity
        '''
        
        if is_cubic:
            return CommonBigO.CUBIC
        return CommonBigO.NON_COMMON
    
    def exponential(self, func) -> CommonBigO:
        is_exponential = False
        
        '''
        TODO: function that checks if algorithm has exponential complexity
        '''
        
        if is_exponential:
            return CommonBigO.EXPONENTIAL
        return CommonBigO.NON_COMMON
    
    def factorial(self, func) -> CommonBigO:
        is_factorial = False
        
        '''
        TODO: function that checks if algorithm has factorial complexity
        '''
        
        if is_factorial:
            return CommonBigO.FACTORIAL
        return CommonBigO.NON_COMMON
    
    def _calculate_complexity(self, func) -> CommonBigO:
        checking_funcs = [
            self.constant,
            self.linear,
            self.logarithmic,
            self.linearithmic,
            self.quadratic,
            self.cubic,
            self.exponential,
            self.factorial,
        ]
        
        _complexities = []
        for _check in checking_funcs:
            if (_complexity := _check(func)) is not CommonBigO.NON_COMMON:
                _complexities.append(_complexity)
        
        if _complexities:
            # returns the minimum from the list of possible complexities
            return _complexities[0]
        
        # if all checking funcs returns CommonBigO.NON_COMMON
        return CommonBigO.NON_COMMON
    
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