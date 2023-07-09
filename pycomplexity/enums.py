from enum import Enum

'''
Notation format enum
'''
class NotationFormat(Enum):
    
    BIG_O : str = 'BIG O'
    BIG_OMEGA : str = 'BIG Ω (OMEGA)'
    BIG_THETA : str = 'BIG Θ (THETA)'
    
    def __str__(self) -> str:
        return self.value
    

'''
The most common Big O complexity notations enum
'''
class CommonBigO(Enum):
    
    NON_COMMON : str = 'Non common'
    CONSTANT : str = '1'
    LINEAR : str = 'N'
    LOGARITHMIC : str = 'log(N)'
    LINEARITHMIC : str = 'N*log(N)'
    QUADRATIC : str = 'N^2'
    CUBIC : str = 'N^3'
    EXPONENTIAL : str = '2^N'
    FACTORIAL : str = 'N!'

    def __str__(self) -> str:
        if self is not self.NON_COMMON:
            return f'O({self.value})'
        return self.value
    
    def __repr__(self) -> str:
        _formatted = self.name.replace('_', ' ').capitalize()
        return f'{_formatted} time complexity'