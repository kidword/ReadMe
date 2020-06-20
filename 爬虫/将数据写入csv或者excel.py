import pandas as pd

# 定义数据
temp = []

for tes in tes_list:
    temp.append([tes['name'], tes['age'], tes['value']])
    
result = pd.DataFrame(tem)
# 定义列名
result.colums = ['name', 'age', 'value']

result.to_excel('China_{}.xls'.format('123'),  index=False)  # 写入excel
result.to_csv('China_{}.xls'.format('123'),  index=False)  # 写入csv
