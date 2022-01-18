import streamlit as st
import pandas as pd
import numpy as np

#Muda o layout da pagina aproveitando mais o espaço de tela
st.set_page_config(layout='wide')

#Armazena o dataset em cache
st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)

    return data

#get data
path = '/home/daniel/repos/curso_python_zero_ao_ds/datasets/kc_house_data.csv'
data = get_data(path)

#add new features
data['price_m2'] = data['price'] / data['sqft_lot']

# ==================
# Data overview
# ==================
f_attributes = st.sidebar.multiselect('Enter columns', data.columns)
f_zipcode = st.sidebar.multiselect('Enter zipcode', data['zipcode'].unique())

st.title('Data Overview')

if(f_zipcode != []) & (f_attributes != []):
    data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]

elif(f_zipcode != []) & (f_attributes == []):
    data = data.loc[data['zipcode'].isin(f_zipcode), :]

elif(f_zipcode == []) & (f_attributes != []):
    data = data.loc[:, f_attributes]

else:
    data = data.copy()

# Average metrics
df1 = data[['id', 'zipcode']].groupby('zipcode').count().reset_index()
df2 = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
df3 = data[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()
df4 = data[['price_m2', 'zipcode']].groupby('zipcode').mean().reset_index()

#merge
m1 = pd.merge(df1, df2, on='zipcode', how='inner')
m2 = pd.merge(m1, df3, on='zipcode', how='inner')
df = pd.merge(m2, df4, on='zipcode', how='inner')

df.columns = ['ZIPCODE', 'TOTAL HOUSES', 'PRICES', 'SQFT LIVING', 'PRICE/M2']

st.dataframe(df, height=600 )

#Statistic Descriptive
num_attributes = data.select_dtypes(include=['int64', 'float64'])
media = pd.Dataframe(num_attributes.apply(np.mean))
mediana = pd.Dataframe(num_attributes.apply(np.median))
std = pd.Dataframe(num_attributes.apply(np.std))


#st.write(data.head())
