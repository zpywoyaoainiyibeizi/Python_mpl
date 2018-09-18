import numpy as np
import pandas as pd

def To_txt():

    df = pd.read_excel('0918.xls',usecols=[0,1,2,3])
    df.to_csv('excel_to_python.csv')
    df_1 = pd.DataFrame(pd.read_csv('excel_to_python.csv', header=1))
    df_1.dropna(axis=0).to_csv('excel_to_python.txt',sep='\t')

    with open( 'excel_to_python.txt', 'r', encoding='utf-8') as qingxi:
        with open('excel_to_python_res.txt', 'w', encoding='utf-8') as write_file:
            for line in qingxi:
                print (line)
                row = line.split('\t')
                index0 = row[0]
                index1 = row[1]
                index2 = row[2]
                index3 = row[3]
                index4 = row[4]
                index5 = row[5]
                if index2 =='品名':
                    continue
                else:
                    write_line=index2+'\t'+index3+'\t'+index4+'\t'+index5
                    write_file.write(write_line)

To_txt()