import os
import pandas as pd
name_list=[]
res_list=[]
xls_name='0918.xls'
csv_name='pandas_csv.csv'
csv_txt_name='pandas_csv_txt.txt'
csv_res_name='0918'



def file_read():

    # 读取excel文件前四列
    df = pd.read_excel(xls_name, usecols=[0, 1, 2, 3])
    # 生成csv文件(为了清洗)
    df.to_csv(csv_name)

    df_1 = pd.DataFrame(pd.read_csv(csv_name, header=1))
    # 去除空值列
    df_1.dropna(axis=0).to_csv(csv_txt_name, sep='\t')
    # 清洗数据
    with open(csv_txt_name, 'r', encoding='utf-8') as qingxi:
        with open(csv_res_name+'.txt', 'w', encoding='utf-8') as write_file:
            for line in qingxi:
                print(line)
                row = line.split('\t')
                index2 = row[2]
                index3 = row[3]
                index4 = row[4]
                index5 = row[5]
                if index2 == '品名':
                    continue
                else:
                    write_line = index2 + '\t' + index3 + '\t' + index4 + '\t' + index5
                    write_file.write(write_line)
    # 菜品去重 添加进name_list
    with open(csv_res_name+'.txt','r',encoding='utf-8') as De_weighting:
        for line in De_weighting:
            real_line = line.strip()
            row = real_line.split('\t')
            index0 = row[0]
            if index0 not in name_list:
                name_list.append(index0)
    # 将文件拆分为 每个菜品一个的小文件
    for name in name_list:
        with open(csv_res_name+'.txt', 'r', encoding='utf-8') as file:
            with open(name + '.txt', 'w', encoding='utf-8') as write_file:
                for line in file:
                    real_line = line.strip()
                    row = real_line.split('\t')
                    index0 = row[0]
                    if index0 == name:
                        write_file.write(line)
                    else:
                        continue
    shuliang_float = 0
    zongjia_float = 0
    # 统计菜品的数量和总价，求出均价
    for name in name_list:
        with open(name+'.txt','r',encoding='utf-8') as read_file:
           for line in read_file:
               real_line = line.strip()
               row = real_line.split('\t')
               index1 = float (row[1])
               index3 = float (row[3])
               shuliang_float=shuliang_float+index1
               zongjia_float=zongjia_float+index3
        junjia=zongjia_float/shuliang_float
        Quantity=float('%.2f' % shuliang_float)
        Total_price=float('%.2f' % zongjia_float)
        Average_price=float('%.2f' % junjia)
        write_line=name+'\t'+str(Quantity)+'\t'+str(Average_price)+'\t'+str(Total_price)
        res_list.append(write_line)
        shuliang_float = 0
        zongjia_float = 0
        os.remove(name+'.txt')
    # 打印结果
    with open(csv_res_name+'_res.txt','w',encoding='utf-8') as write_file:
        for line in res_list:
            write_file.write(line+'\n')
        os.remove(csv_name)
        os.remove(csv_txt_name)
        os.remove(csv_res_name+'.txt')



file_read()