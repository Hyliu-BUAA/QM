import re
import os
import csv

# python3 -m sns_mp2_test.utilitys.inputFileWriter
from ..parameters import inputFileConfig


class InputFileWriter(object):
    def __init__(self,
                lsts_1:list, 
                lsts_2:list,
                input_file_psi4_path:str=inputFileConfig.input_file_psi4_path):
        self.lsts_1 = lsts_1
        self.lsts_2 = lsts_2
        
        self.tmp_input_file_psi4_path = "./tmp.csv"
        
        try:
            os.mknod(self.tmp_input_file_psi4_path)
        except:
            pass
        
        self.input_file_psi4_path = input_file_psi4_path
    
    
    def write(self):
        with open(self.tmp_input_file_psi4_path, "a", newline="") as f:
            ### 1. 写入 `molecule {`
            f.write("molecule {\n")
            
            ### 2. 写入第一个分子的 `元素` 和 `坐标``
            csv_writer = csv.writer(f)

            for i in range( len(self.lsts_1[0]) ):
                # print(type())
                csv_writer.writerow( [self.lsts_1[0][i]] + self.lsts_2[0][i] )

            ### 3. 顶格写入 `--`
            f.write("--\n")
        
        
            ### 4. 写入第二个分子的 `元素` 和 `坐标``
            csv_writer = csv.writer(f)
            for i in range( len(self.lsts_1[1]) ):
                csv_writer.writerow( [self.lsts_1[1][i]] + self.lsts_2[1][i] )
            
            
            ### 5. 写入 `}`
            f.write("}\n\n")
            
            ### 6. 写入 `import`
            f.write("import snsmp2\n")
            f.write("energy('sns-mp2')")
        
        f_tmp = open(self.tmp_input_file_psi4_path, "r+")
        f = open(self.input_file_psi4_path, "a")
        
        for row in f_tmp.read():
            row_content = re.sub(',', '\t', row)
            f.write(row_content)
        
        f_tmp.close()
        f.close()
        os.remove(self.tmp_input_file_psi4_path)


if __name__ == "__main__":
    lst_1 = [[1, 2, 3], [11, 12, 13]]
    lst_2 = [ [[4, 5], [6, 7], [8, 9]], 
              [[4, 5], [6, 7], [8, 9]]]
    input_file_writer = InputFileWriter(lst_1, lst_2)
    input_file_writer.write()