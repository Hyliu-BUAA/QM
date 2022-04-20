# python3 -m sns_mp2_test.engine.generateInput
from ..utilitys.inputFileWriter import InputFileWriter
from ..extract.extract import FormulasExtractor
from ..extract.extract import CoordinationsExtractor


def generate_inputs():
    formula_extractor = FormulasExtractor()
    lsts_1 = formula_extractor.get_formulas_lst()
    
    
    coordiantions_extractor = CoordinationsExtractor()
    lsts_2 = coordiantions_extractor.get_formulas_coordinations_lst()

    
    input_file_writer = InputFileWriter(lsts_1, lsts_2)
    input_file_writer.write()
    

if __name__ == "__main__":
    generate_inputs()    