# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)


import pandas as pd

df = pd.read_csv('california_housing_train.csv')

print(df[(df['population'] < 500) & (df['population'] >= 0)].mean()['median_house_value']) # в точном соответствии с условием.

print(df[df['population'] < 500].mean()['median_house_value']) # если точно знать, что эти данные всегда будут "люди", то можно и так.

