import numpy as np
import pandas as pd

# python3 -m sns_mp2_test.extract.extract
# params
from ..parameters import extractConfig
from ..cores.formula import Formula
from ..cores.coordination import Coordinations



class FormulasExtractor(object):
    '''
    Description
    -----------

    Attributes
    ----------
        1. self.elements_lst: list of str
            所有元素（多种化合物）的元素列表
    '''
    def __init__(self,
                DES_csv_path:str=extractConfig.DES_csv_path,
                row:int=extractConfig.row):
        df = pd.read_csv(DES_csv_path)
        # type(elements) = str
        self.elements_lst = df.loc[row, "elements"].split()
        self.natoms_0 = df.loc[row, "natoms0"]
        self.natoms_1 = df.loc[row, "natoms1"]
    
    def get_formulas_lst(self):
        formulas_elements_lst = [self.elements_lst[:self.natoms_0],
                                self.elements_lst[self.natoms_0:]]
        
        formulas_lst = [ formulas_elements_lst[0], 
                        formulas_elements_lst[1] ]
        
        print(formulas_lst)
        
        return formulas_lst
            

class CoordinationsExtractor(object):
    def __init__(self,
                DES_csv_path:str=extractConfig.DES_csv_path,
                row:int=extractConfig.row):
        df = pd.read_csv(DES_csv_path)
        self.coordinations_lst = df.loc[row, "xyz"].split()
        
        self.natoms_0 = df.loc[row, "natoms0"]
        self.natoms_1 = df.loc[row, "natoms1"]
        
    
    def get_formulas_coordinations_lst(self):
        # formulas_coordinations_lst: 三维数组
        #   每个二维数组代表一个formula的所有原子坐标
        formulas_coordinations_lst = [self.coordinations_lst[:self.natoms_0 * 3],
                                self.coordinations_lst[(self.natoms_0 * 3):]]
        #formulas_coordinations_lst = [np.matrix(xyz_lst).reshape(-1, 3).astype(np.float32) for xyz_lst in formulas_coordinations_lst]
        formulas_coordinations_lst = [np.array(xyz_lst).reshape(-1, 3) for xyz_lst in formulas_coordinations_lst]
        formulas_coordinations_lst = [array.tolist() for array in formulas_coordinations_lst]

        
        formulas_coordinations_lst = [ formulas_coordinations_lst[0],
                                       formulas_coordinations_lst[1] ]
        
        print(formulas_coordinations_lst)
        
        return formulas_coordinations_lst


if __name__ == "__main__":
    formula_extractor = FormulasExtractor()
    print(formula_extractor.get_formulas_lst())
    
    coordiantions_extractor = CoordinationsExtractor()
    print( coordiantions_extractor.get_formulas_coordinations_lst() )