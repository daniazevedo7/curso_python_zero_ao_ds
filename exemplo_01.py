import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

#mostre na tela as 5 primeiras linha do dataset
#print(data.head())

#mostre o numero de linhas e colunas do dataset
#print(data.shape)

#Quantos atributos as casas possuem?
#print(data.columns)

#4. Qual a casa mais cara ( casa com o maior valor de venda )?
#print(data[['id', 'price']].sort_values('price', ascending=False ))

#5. Qual a casa com o maior número de quartos?
#print(data[['id', 'bedrooms']].sort_values('bedrooms', ascending= False))

#Qual a soma total de quartos do conjunto de dados?
#print(sum(data.bedrooms))

# 7. Quantas casas possuem 2 banheiros?
#df_filter = data[['id', 'bathrooms']].loc[data['bathrooms'] == 2]
# num_houses = len(df_filter)
# print(df_filter)
# print('****',num_houses,'****')

# #Qual o preço médio de todas as casas no conjunto de dados?
# print(data.describe())
# print(data['price'].mean())

#9. Qual o preço médio de casas com 2 banheiros?
# df_filter = data[['id', 'bathrooms', 'price']].loc[data['bathrooms']== 2]
# print(df_filter)
#print(df_filter['price'].mean())

#10. Qual o preço mínimo entre as casas com 3 quartos?
# df_filter = data[['id','bedrooms', 'price']].loc[data['bedrooms']==3]
# #print(df_filter.head())
# print(df_filter[['id','price', 'bedrooms']].sort_values('price', ascending=False))
# print(df_filter['price'].min())

#12. Quantas casas tem mais de 2 andares?
df_filter = data['id', 'floor'].loc[data['floor'] == ]

