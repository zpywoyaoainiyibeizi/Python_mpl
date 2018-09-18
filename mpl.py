import os
name_list=[]
res_list=[]
path_name='name_number_price'
def file_read():
    with open(path_name+'.txt','r',encoding='utf-8') as De_weighting:
        for line in De_weighting:
            real_line = line.strip()
            row = real_line.split('\t')
            index0 = row[0]
            if index0 not in name_list:
                name_list.append(index0)

    for name in name_list:
        with open(path_name+'.txt', 'r', encoding='utf-8') as file:
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
    for name in name_list:
        with open(name+'.txt','r',encoding='utf-8') as read_file:
           for line in read_file:
               real_line = line.strip()
               row = real_line.split('\t')
               index0 = row[0]
               index1 = float (row[1])
               index2 = float (row[2])
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

    with open(path_name+'_res.txt','w',encoding='utf-8') as write_file:
        for line in res_list:

            write_file.write(line+'\n')

file_read()