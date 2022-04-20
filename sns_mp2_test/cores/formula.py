class Formula(object):
    '''
    Description
    -----------
        一个化合物的化学式
    
    Attributes
    ----------
        1. self.elements_lst: list
            化学式所有元素（包含重复）组成的列表
    '''
    def __init__(self, elements_lst:list):
        self.elements_lst = elements_lst
    
    
    def __repr__(self):
        print(self.elements_lst)
        return ""
    
    
    def __str__(self):
        return self.__repr__()
    

    def from_smiles_string(self, smiles_string):
        pass