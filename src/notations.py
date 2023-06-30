import inspect
from typing import List, Optional

from .analysis import Analyzer, AnalysisFormatter, NotationFormat


'''
Base class of asymptotic notation
'''
class Notation:

    def __init__(self) -> None:
        self.code_to_analyse : List[str] = []
    
    def __repr__(self) -> str:
        return '\n'.join(self.code_to_analyse)
    
    def _code_to_string(self, func):
        def wrapper(*args, **kwargs) -> Optional[str]:
            code = inspect.getsource(func)
            code_lines = code.split('\n')[1:]
            modified_code = '\n'.join(code_lines)
            self.code_to_analyse.append(modified_code)
            return self.code_to_analyse
        return wrapper
    
    def get_code(self, func):
        return self._code_to_string(func)()
    
    def report(func):
        def wrapper(self, *args, **kwargs):
            analysis_formatter: AnalysisFormatter = func(self, *args, **kwargs)
            return analysis_formatter.report()
        return wrapper


'''
Implementation of Big O notation
'''
class BigO(Notation):

    def __init__(self) -> None:
        super().__init__()
    
    @Notation.report
    def complexity(self, func) -> AnalysisFormatter:
        
        return AnalysisFormatter(
            notation_format=NotationFormat.BIG_O,
        )
        


'''
Implementation of Big Omega notation
'''
class BigOmega(Notation):
    
    def __init__(self) -> None:
        super().__init__()
    
    @Notation.report
    def complexity(self, func) -> AnalysisFormatter:
        
        return AnalysisFormatter(
            notation_format=NotationFormat.BIG_OMEGA,
        )
        
        
'''
Implementation of Big Theta notation
'''
class BigTheta(Notation):
    
    def __init__(self) -> None:
        super().__init__()
    
    @Notation.report
    def complexity(self, func) -> AnalysisFormatter:
        
        return AnalysisFormatter(
            notation_format=NotationFormat.BIG_THETA,
        )