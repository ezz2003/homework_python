# Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
#
#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |


import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)
x = pd.get_dummies(data, columns=['whoAmI'])
print(x)

m = data[data.columns[0]].tolist()
unic_str = [m[0]]
for i in range(1, len(m)):
    if m[i] not in unic_str:
        unic_str.append(m[i])

d_f = {}
for i in range(len(unic_str)):
    m_v = [1 if unic_str[i] == m[0] else 0]
    for j in range(1, len(m)):
        if m[j] == m[0]:
            m_v.append(m_v[0])
        else:
            m_v.append(int(not m_v[0]))
    d_f[f'whoAmI_{unic_str[i]}'] = m_v
d_ff = pd.DataFrame(d_f)
print(d_ff)
