class Coordinations(object):
    '''
    Description
    -----------
        化学式的原子坐标 (和 `Formula.elements_lst` 中的元素一一对应)
    
    Attributes
    ----------
        1. 
    '''
    def __init__(self, coordinations_lst:list):
        self.coordinations_lst = coordinations_lst
        
        
    def __repr__(self):
        print(self.coordinations_lst)
        return ""
    

    def __str__(self):
        return self.__repr__()

    def from_smiles_string(self):
        pass