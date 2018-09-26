import pandas as pd

def To_txt():
    name_list=[]
    df = pd.read_excel('菜谱.xls',usecols=[1,2,3])
    df.to_csv('Acceptance_statistics.csv')
    df_1 = pd.DataFrame(pd.read_csv('Acceptance_statistics.csv', header=1))
    df_1.dropna(axis=0).to_csv('Acceptance_statistics.txt',sep='\t')

    with open('Acceptance_statistics.txt', 'r', encoding='utf-8') as qingxi:
        with open('Acceptance_statistics_res.txt', 'w', encoding='utf-8') as write_file:
            for line in qingxi:
                row = line.split('\t')

                index3 = row[2]

                index4 = row[3]
                index5 = row[4]
                if index3 == '早':
                    continue
                else:
                    write_line = index3+'、' + index4 +'、'+ index5+'、'
                    write_file.write(write_line.strip()+'\n')

     # 菜品去重 添加进name_list
    with open('Acceptance_statistics_res.txt', 'r', encoding='utf-8') as De_weighting:
        for line in De_weighting:
            real_line = line.strip()
            row = real_line.split('、')
            for dish_name in row:
                if dish_name not in name_list:
                    name_list.append(dish_name)
    #打印菜名：
    with open('Acceptance_statistics_name.txt', 'w', encoding='utf-8') as file:
        for name in name_list:
            file.write(name+'\n')


To_txt()