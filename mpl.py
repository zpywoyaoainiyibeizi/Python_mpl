
name_list=[]
res_list=[]
chaifen_list=[]
def file_read():
    with open('name.txt','r',encoding='utf-8') as f:
        for line in f:
            real_line=line.strip()
            name_list.append(real_line)

        for name in name_list:
            with open('name_number_price.txt', 'r', encoding='utf-8') as file:
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
               index1 = float(row[1])
               index2 = float (row[2])
               index3 = float (row[3])
               shuliang_float=shuliang_float+index1
               zongjia_float=zongjia_float+index3
        junjia=zongjia_float/shuliang_float
        write_line=name+'\t'+str(shuliang_float)+'\t'+str(junjia)+'\t'+str(zongjia_float)
        res_list.append(write_line)
        shuliang_float = 0
        zongjia_float = 0
    with open('res.txt','w',encoding='utf-8') as write_file:
        for line in res_list:

            write_file.write(line+'\n')
file_read()