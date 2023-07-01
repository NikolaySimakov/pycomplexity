from enum import Enum

'''
Notation format enum
'''
class NotationFormat(Enum):
    
    BIG_O : str = 'BIG O'
    BIG_OMEGA : str = 'BIG Ω (OMEGA)'
    BIG_THETA : str = 'BIG Θ (THETA)'
    
    def __str__(self) -> str:
        return str(self.value)